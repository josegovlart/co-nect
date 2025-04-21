import customtkinter as ctk
from styles import theme
from session.auth import getSession


class AdminHomeScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.configure(fg_color=theme.BACKGROUND_COLOR)

        self.frameBack = ctk.CTkFrame(self, fg_color="transparent")
        self.frameBack.pack(padx=30, pady=(20, 0), anchor="w")

        self.userGreeting = ctk.StringVar()

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

        self.labelTitle = ctk.CTkLabel(
            self,
            textvariable=self.userGreeting,
            text_color=theme.PRIMARY_COLOR,
            font=theme.TITLE_FONT
        )
        self.labelTitle.pack(anchor="w", padx=30, pady=(20, 10))

    def goBack(self):
        self.controller.show_frame(self.controller.__class__)

    def onShow(self):
        self.userGreeting.set(f"Olá, (admin) {getSession()["name"]}")