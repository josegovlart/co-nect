import customtkinter as ctk
from styles import theme
from session.auth import login
from views.clientHomeScreen import ClientHomeScreen
from views.adminHomeScreen import AdminHomeScreen


class LoginScreen(ctk.CTkFrame):
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

        self.labelTitle = ctk.CTkLabel(
            self,
            text="Co-Nect",
            text_color=theme.PRIMARY_COLOR,
            font=theme.TITLE_FONT
        )
        self.labelTitle.pack(anchor="w", padx=30, pady=(20, 10))

        self.entryEmail = self.createInput("Email", "Digite seu email")
        self.entryPassword = self.createInput("Senha", "Digite sua senha", show="*")

        self.labelStatus = ctk.CTkLabel(self, text="", text_color="red")
        self.labelStatus.pack(pady=(10, 0))

        self.btnCreate = ctk.CTkButton(
            self,
            text="Entrar",
            hover_color=theme.PRIMARY_COLOR_HOVER,
            corner_radius=3,
            fg_color=theme.PRIMARY_COLOR,
            command=self.login
        )
        self.btnCreate.pack(padx=30, pady=(20, 0), fill="x")

        self.frameLoginLink = ctk.CTkFrame(self, fg_color="transparent")
        self.frameLoginLink.pack(pady=(20, 0))

    def login(self):
        email = self.entryEmail.get()
        password = self.entryPassword.get()

        if not email or not password:
            self.labelStatus.configure(text="Preencha todos os campos", text_color="red")
            return

        success, message, type = login(email, password)

        if success:
            self.labelStatus.configure(text=message, text_color="green")
            self.goToHomeScreen(type)
        else:
            self.labelStatus.configure(text=message, text_color="red")

    def createInput(self, label_text, placeholder, show=None, entry_options={}, label_options={}):
        label = ctk.CTkLabel(
            self,
            text=label_text,
            font=theme.LABEL_FONT,
            text_color=theme.PRIMARY_COLOR,
            **label_options
        )
        label.pack(anchor="w", padx=30, pady=(10, 0))

        entry = ctk.CTkEntry(
            self,
            border_width=0,
            fg_color=theme.INPUT_COLOR,
            placeholder_text=placeholder,
            show=show,
            **entry_options
        )
        entry.pack(padx=30, fill="x")

        border = ctk.CTkFrame(self, height=1.5, fg_color=theme.SECONDARY_COLOR)
        border.pack(fill="x", padx=30, pady=(0, 10))

        return entry


    def goToHomeScreen(self, type):
        if type == "admin":
            self.controller.show_frame(AdminHomeScreen)
        else:
            self.controller.show_frame(ClientHomeScreen)

    def goBack(self):
        self.controller.show_frame(self.controller.__class__)