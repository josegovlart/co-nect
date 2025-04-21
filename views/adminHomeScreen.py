import customtkinter as ctk
from styles import theme
from session.auth import getSession


class AdminHomeScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.userGreeting = ctk.StringVar()

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

        self.labelSpaces = ctk.CTkLabel(
            self,
            text="Meus espaços",
            text_color=theme.TEXT_COLOR,
            font=theme.LABEL_FONT
        )
        self.labelSpaces.pack(anchor="w", padx=30, pady=(20, 10))

        self.btnCreate = ctk.CTkButton(
            self,
            text="Adicionar espaço",
            hover_color=theme.PRIMARY_COLOR_HOVER,
            corner_radius=3,
            fg_color=theme.PRIMARY_COLOR,
            command=self.goToCreateRoom
        )
        self.btnCreate.pack(padx=30, pady=(20, 0), fill="x")

        self.btnReports = ctk.CTkButton(
            self,
            text="Ver relatórios",
            hover_color=theme.TRANSPARENT_HOVER,
            text_color=theme.PRIMARY_COLOR,
            corner_radius=3,
            fg_color=theme.BACKGROUND_COLOR,
            command=self.goToReports
        )
        self.btnReports.pack(padx=30, pady=(20, 0), fill="x")

    def goBack(self):
        self.controller.show_frame(self.controller.__class__)

    def onShow(self):
        self.userGreeting.set(f"Olá, {getSession()["name"]}")

    def goToCreateRoom(self):
        print("Bora criar a sala")

    def goToReports(self):
        print("Bora ver esses relatórios")