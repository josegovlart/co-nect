import customtkinter as ctk
from styles import theme
from PIL import Image, ImageTk
from session.auth import login
from views.adminHomeScreen import AdminHomeScreen
from controllers.reservation import ReservationController


class ReservationDetailsScreen(ctk.CTkFrame):
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

        self.labelBack.bind("<Button-1>", lambda e: self.goToHomeScreen())

        self.labelTitle = ctk.CTkLabel(
            self,
            text="Detalhes da Reserva",
            text_color=theme.PRIMARY_COLOR,
            font=theme.TITLE_FONT
        )
        self.labelTitle.pack(anchor="w", padx=30, pady=(20, 10))

        image = Image.open("assets/placeholder.png")
        image = image.resize((250, 150))
        photo = ImageTk.PhotoImage(image)

        image_label = ctk.CTkLabel(self, image=photo, text="")
        image_label.image = photo
        image_label.place(x=30, y=60)

        ctk.CTkLabel(self, text="Data", font=("Arial", 14, "bold")).place(x=30, y=390)
        self.date_entry = ctk.CTkEntry(self, placeholder_text="Ex: 24/05/2025")
        self.date_entry.place(x=30, y=430)

        ctk.CTkLabel(self, text="Horário", font=("Arial", 14, "bold")).place(x=30, y=470)
        self.time_entry = ctk.CTkEntry(self, placeholder_text="Ex: 09:00")
        self.time_entry.place(x=30, y=500)

        self.labelStatus = ctk.CTkLabel(self, text="", text_color="red", wraplength=250)
        self.labelStatus.place(x=50, y=540)

        reschedule_button = ctk.CTkButton(
            self,
            text="Atualizar reserva",
            fg_color=theme.PRIMARY_COLOR,
            hover_color=theme.PRIMARY_COLOR_HOVER,
            width=260,
            height=30,
            command=self.handle_reschedule_click_wrapper
        )
        reschedule_button.place(x=30, y=570)

    def set_data(self, reservationId):
        reservationData = ReservationController.getReservationById(reservationId)
        self.reservationId = reservationId
        roomName = reservationData["room"]["name"]
        roomAddress = reservationData["room"]["address"]
        roomHourlyRate = reservationData["room"]["price"]
        duration = reservationData["duration"]
        reservationPrice = roomHourlyRate * duration

        ctk.CTkLabel(self, text=f"Duração: {duration}h", font=("Arial", 14, "bold"), text_color="black").place(x=30, y=340)
        ctk.CTkLabel(self, text=f"{roomName}", font=("Arial", 18, "bold"), text_color="black").place(x=30, y=250)
        ctk.CTkLabel(self, text=f"{roomAddress}", font=("Arial", 12), text_color="gray").place(x=30, y=280)
        ctk.CTkLabel(self, text=f"R${reservationPrice:.2f}", font=("Arial", 12, "bold"), text_color="black").place(x=30, y=300)

    def handle_reschedule_click_wrapper(self):
        reservation_id = self.reservationId
        date = self.date_entry.get()
        time = self.time_entry.get()
        self.handle_reschedule_click(reservation_id, date, time)

    def handle_reschedule_click(self, reservation_id, date, time):
        success, message = ReservationController.reschedule_reservation(reservation_id, date, time)
        self.show_message(success, message)

    def show_message(self, success, message):
        self.labelStatus.configure(text=message, text_color=("green" if success else "red"))

    def goToHomeScreen(self):
        from views.clientHomeScreen import ClientHomeScreen
        self.controller.show_frame(ClientHomeScreen)

    def goBack(self):
        self.controller.show_frame(self.controller.__class__)