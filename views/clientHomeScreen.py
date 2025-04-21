import customtkinter as ctk
from styles import theme
from session.auth import getSession


class ClientHomeScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.configure(fg_color=theme.BACKGROUND_COLOR)

        self.frameBack = ctk.CTkFrame(self, fg_color="transparent")
        self.frameBack.pack(padx=30, pady=(20, 0), anchor="w")

        self.userGreeting = ctk.StringVar()

        self.labelTitle = ctk.CTkLabel(
            self,
            text="Co-Nect",
            text_color=theme.PRIMARY_COLOR,
            font=theme.TITLE_FONT
        )
        self.labelTitle.pack(anchor="w", padx=30, pady=(20, 10))

        self.labelGreeting = ctk.CTkLabel(
            self,
            textvariable=self.userGreeting,
            text_color=theme.TEXT_COLOR,
            font=theme.TITLE_FONT
        )
        self.labelGreeting.pack(anchor="w", padx=30, pady=(20, 10))

        self.labelReservations = ctk.CTkLabel(
            self,
            text="Minhas reservas",
            text_color=theme.TEXT_COLOR,
            font=theme.LABEL_FONT
        )
        self.labelReservations.pack(anchor="w", padx=30, pady=(20, 10))

        self.labelRooms = ctk.CTkLabel(
            self,
            text="Salas disponíveis",
            text_color=theme.TEXT_COLOR,
            font=theme.LABEL_FONT
        )
        self.labelRooms.pack(anchor="w", padx=30, pady=(20, 10))

    def onShow(self):
        self.userGreeting.set(f"Olá, {getSession()["name"]}")