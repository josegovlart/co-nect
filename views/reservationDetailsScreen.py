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

        ctk.CTkLabel(self, text="Duração", font=("Arial", 14, "bold"), text_color="black").place(x=30, y=340)
        self.duration = ctk.CTkOptionMenu(self, fg_color=theme.BACKGROUND_COLOR, values=["1h", "2h", "3h", "4h"],
                                          text_color=theme.TEXT_COLOR)
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

    def set_data(self, reservationId):
        reservationData = ReservationController.getReservationById(reservationId)

        roomName = reservationData["room"]["name"]
        roomAddress = reservationData["room"]["address"]
        roomHourlyRate = reservationData["room"]["price"]
        reservationPrice = roomHourlyRate * reservationData["duration"]

        ctk.CTkLabel(self, text=f"{roomName}", font=("Arial", 18, "bold"), text_color="black").place(x=30, y=250)
        ctk.CTkLabel(self, text=f"{roomAddress}", font=("Arial", 12), text_color="gray").place(x=30, y=280)
        ctk.CTkLabel(self, text=f"{reservationPrice}", font=("Arial", 12, "bold"), text_color="black").place(x=30, y=300)


    def goToHomeScreen(self):
        from views.clientHomeScreen import ClientHomeScreen
        self.controller.show_frame(ClientHomeScreen)

    def goBack(self):
        self.controller.show_frame(self.controller.__class__)