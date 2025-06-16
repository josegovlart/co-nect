from datetime import datetime
import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk
from session.auth import getSession
from styles import theme
from controllers.reservation import ReservationController
from utils.validations import validate_reservation_fields, is_after_now, is_valid_date_format, is_valid_time_format
from views.paymentPopUp import PaymentPopup


class CreateReservationScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.configure(fg_color=theme.BACKGROUND_COLOR)

        self.frameBack = ctk.CTkFrame(self, fg_color="transparent")
        self.frameBack.pack(padx=30, pady=(20, 0), anchor="w")

        self.labelBack = ctk.CTkLabel(
            self.frameBack,
            fg_color="#ede7fb",
            text="←",
            corner_radius=20,
            text_color=theme.PRIMARY_COLOR,
            font=theme.LABEL_FONT
        )
        self.labelBack.pack(expand=True)
        self.labelBack.bind("<Button-1>", lambda e: self.goBack())

        image = Image.open("assets/placeholder.png")
        image = image.resize((250, 150))
        photo = ImageTk.PhotoImage(image)

        image_label = ctk.CTkLabel(self, image=photo, text="")
        image_label.image = photo
        image_label.place(x=30, y=60)
        
        ctk.CTkLabel(self, text="Duração", font=("Arial", 14, "bold"), text_color="black").place(x=30, y=340)
        self.duration = ctk.CTkOptionMenu(
            self, 
            fg_color=theme.BACKGROUND_COLOR, 
            values=["1h", "2h", "3h", "4h"], 
            text_color=theme.TEXT_COLOR,
            command=self.update_total_price
        )
        self.duration.set("2h")
        self.duration.place(x=30, y=370)

        ctk.CTkLabel(self, text="Data", font=("Arial", 14, "bold")).place(x=30, y=420)
        self.date_entry = ctk.CTkEntry(self, placeholder_text="Ex: 24/05/2025")
        self.date_entry.place(x=30, y=450)

        ctk.CTkLabel(self, text="Horário", font=("Arial", 14, "bold")).place(x=30, y=500)
        self.time_entry = ctk.CTkEntry(self, placeholder_text="Ex: 09:00")
        self.time_entry.place(x=30, y=530)

        self.labelStatus = ctk.CTkLabel(self, text="", text_color="red")
        self.labelStatus.place(x=50, y=570)

        reserve_button = ctk.CTkButton(self, text="Reservar", fg_color=theme.PRIMARY_COLOR, hover_color=theme.PRIMARY_COLOR_HOVER, width=260, height=30, command=self.reserve)
        reserve_button.place(x=30, y=600)

    def reserve(self):
        date = self.date_entry.get()
        time = self.time_entry.get()

        is_valid, message = validate_reservation_fields(date, time)

        duration = int(self.duration.get().replace('h', ''))
        room = self.room
        latestReceipt = "IMPLEMENTAR"  # implementar isso

        date_valid = is_valid_date_format(date)
        if is_valid:
            if date_valid:
                time_valid = is_valid_time_format(time)
                if time_valid:
                    after_now = is_after_now(date + " " + time)
                    if after_now:
                        dt = datetime.strptime(date + " " + time, "%d/%m/%Y %H:%M")
                        formattedDatetime = dt.strftime("%Y-%m-%d %H:%M")
                        is_available = ReservationController.is_room_available(self.room["id"], formattedDatetime, duration)
                        if is_available:
                            self.labelStatus.configure(text="")
                            PaymentPopup(self, formattedDatetime, duration, room, latestReceipt, self.complete_reservation)
                        else:
                            self.showRedMessage("O horário escolhido não está disponível. \nEscolha outro horário ou outra data.")
                    else:
                        self.showRedMessage("A data e o horário escolhidos\n devem ser após o dia atual.")
                else:
                    self.showRedMessage("Horário inválido: Use o formato HH:MM.")
            else:
                self.showRedMessage("Data inválida. Use o formato DD/MM/AAAA.")
        else:
            self.showRedMessage(message)
        
    def complete_reservation(self, dateTime, duration, latestReceipt):
        success, client = ReservationController.clientData(getSession()["email"])
        success, message = ReservationController.reserveRoom(dateTime, duration, self.room, latestReceipt, client=client)

        if success:
            self.labelStatus.configure(text=message, text_color="green")

            def clearFields():
                self.date_entry.delete(0, "end")
                self.time_entry.delete(0, "end")
                self.labelStatus.configure(text="")

            self.after(1000, clearFields)
            self.after(1000, self.goBack)
        else:
            self.labelStatus.configure(text=message, text_color="red")

    def set_data(self, reservationData):
        self.reservationName = reservationData["name"]
        self.reservationAddress = reservationData["address"]
        self.reservationPrice = reservationData["price"]
        self.roomId = reservationData["roomId"]

        self.room = ReservationController.getReservationRoomById(self.roomId)

        ctk.CTkLabel(self, text=self.reservationName, font=("Arial", 18, "bold"), text_color="black").place(x=30, y=250)
        ctk.CTkLabel(self, text=self.reservationAddress, font=("Arial", 12), text_color="gray").place(x=30, y=280)
        ctk.CTkLabel(self, text=self.reservationPrice, font=("Arial", 12, "bold"), text_color="black").place(x=30, y=300)

        price_per_hour = float(self.reservationPrice.replace("R$", "").replace("/h", "").strip())
        default_duration = int(self.duration.get().replace('h', ''))
        self.total_price = price_per_hour * default_duration

        self.total_price_label = ctk.CTkLabel(self, text=f"Total: R${self.total_price:.2f}", font=("Arial", 12, "bold"), text_color="black")
        self.total_price_label.place(x=30, y=320)

    def showRedMessage(self, message):
        self.labelStatus.configure(text=message, text_color="red")

    def update_total_price(self, selected_duration):
        price_per_hour = float(self.reservationPrice.replace("R$", "").replace("/h", "").strip())
        duration = int(selected_duration.replace('h', ''))
        total = price_per_hour * duration
        self.total_price_label.configure(text=f"Total: R${total:.2f}")

    def goBack(self):
        from views.clientHomeScreen import ClientHomeScreen
        self.controller.show_frame(ClientHomeScreen)
