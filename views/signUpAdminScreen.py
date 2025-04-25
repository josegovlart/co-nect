import customtkinter as ctk
from controllers.admin import AdminController
from models.admin import Admin
from storage.persistence import saveAdmin
from styles import theme
from utils.validations import validate_admin_signup
from views.loginScreen import LoginScreen
from views.adminHomeScreen import AdminHomeScreen
from session.auth import login


class SignUpAdminScreen(ctk.CTkFrame):
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

        self.entryName = self.createInput("Nome completo", "Digite seu nome completo")
        self.entryEmail = self.createInput("Email", "Digite seu email")
        self.entryCnpj = self.createInput("CNPJ", "Digite seu CNPJ")
        self.entryPassword = self.createInput("Senha", "Digite sua senha", show="*")
        self.entryConfirmPassword = self.createInput("Confirme sua senha", "Confirme sua senha", show="*")

        self.labelStatus = ctk.CTkLabel(self, text="", text_color="red")
        self.labelStatus.pack(pady=(10, 0))

        self.btnCreate = ctk.CTkButton(
            self,
            text="Alugar minhas salas",
            hover_color=theme.PRIMARY_COLOR_HOVER,
            corner_radius=3,
            fg_color=theme.PRIMARY_COLOR,
            command=self.createAccount
        )
        self.btnCreate.pack(padx=30, pady=(20, 0), fill="x")

        self.frameLoginLink = ctk.CTkFrame(self, fg_color="transparent")
        self.frameLoginLink.pack(pady=(20, 0))

        self.loginText = ctk.CTkLabel(
            self.frameLoginLink,
            text="Já tem uma conta?",
            text_color="gray"
        )
        self.loginText.pack(side="left")

        self.loginLink = ctk.CTkLabel(
            self.frameLoginLink,
            text=" Faça login",
            text_color="#4B1CFF",
            cursor="hand2"
        )
        self.loginLink.pack(side="left")
        self.loginLink.bind("<Button-1>", lambda e: self.goToLoginScreen())

    def createAccount(self):
        name = self.entryName.get()
        email = self.entryEmail.get()
        cnpj = self.entryCnpj.get()
        password = self.entryPassword.get()
        confirm_password = self.entryConfirmPassword.get()

        success, message = AdminController.createAdminAccount(name, email, cnpj, password, confirm_password)

        if success:
            self.labelStatus.configure(text=message, text_color="green")
            self.after(2000, lambda: self.loginAndNavigate(email, password))
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

    def goToLoginScreen(self):
        self.controller.show_frame(LoginScreen)

    def loginAndNavigate(self, email, password):
        AdminController.authenticateAdmin(email, password)
        self.controller.show_frame(AdminHomeScreen)

    def goBack(self):
        self.controller.show_frame(self.controller.__class__)
