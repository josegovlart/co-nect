import customtkinter as ctk
from models.admin import Admin
from storage.persistence import saveAdmin
from styles import theme
from utils.validations import validate_admin_signup

class SignUpAdminScreen(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.title("Criar Conta - Administrador")
    self.geometry("329x665")

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("dark-blue")
    self.configure(fg_color=theme.BACKGROUND_COLOR)

    self.frameBack = ctk.CTkFrame(self, fg_color="transparent")
    self.frameBack.pack(padx=30, pady=(20, 0), anchor="w")

    self.labelBack = ctk.CTkLabel(self.frameBack, fg_color="#ede7fb", text="←", corner_radius=20, text_color=theme.PRIMARY_COLOR, font=theme.LABEL_FONT)
    self.labelBack.pack(expand=True)

    self.labelBack.bind("<Button-1>", lambda e: self.goBack())

    self.labelTitle = ctk.CTkLabel(self, text="Co-Nect", text_color=theme.PRIMARY_COLOR, font=theme.TITLE_FONT)
    self.labelTitle.pack(anchor="w", padx=30, pady=(20, 10))

    self.labelName = ctk.CTkLabel(self, text="Nome completo", font=theme.LABEL_FONT, text_color=theme.PRIMARY_COLOR)
    self.labelName.pack(anchor="w", padx=30, pady=(10, 0))
    self.entryName = ctk.CTkEntry(self, border_width=0, fg_color=theme.INPUT_COLOR, placeholder_text="Digite seu nome completo")
    self.entryName.pack(padx=30, fill="x")
    self.entryNameBorder = ctk.CTkFrame(self, height=1.5, fg_color=theme.SECONDARY_COLOR)
    self.entryNameBorder.pack(fill="x", padx=30, pady=(0, 10))

    self.labelEmail = ctk.CTkLabel(self, text="Email", font=theme.LABEL_FONT, text_color=theme.PRIMARY_COLOR)
    self.labelEmail.pack(anchor="w", padx=30, pady=(10, 0))
    self.entryEmail = ctk.CTkEntry(self, border_width=0, fg_color=theme.INPUT_COLOR, placeholder_text="Digite seu email")
    self.entryEmail.pack(padx=30, fill="x")
    self.entryEmailBorder = ctk.CTkFrame(self, height=1.5, fg_color=theme.SECONDARY_COLOR)
    self.entryEmailBorder.pack(fill="x", padx=30, pady=(0, 10))

    self.labelCnpj = ctk.CTkLabel(self, text="CNPJ", font=theme.LABEL_FONT, text_color=theme.PRIMARY_COLOR)
    self.labelCnpj.pack(anchor="w", padx=30, pady=(10, 0))
    self.entryCnpj = ctk.CTkEntry(self, border_width=0, fg_color=theme.INPUT_COLOR, placeholder_text="Digite seu CNPJ")
    self.entryCnpj.pack(padx=30, fill="x")
    self.entryCnpjBorder = ctk.CTkFrame(self, height=1.5, fg_color=theme.SECONDARY_COLOR)
    self.entryCnpjBorder.pack(fill="x", padx=30, pady=(0, 10))

    self.labelPassword = ctk.CTkLabel(self, text="Senha", font=theme.LABEL_FONT, text_color=theme.PRIMARY_COLOR)
    self.labelPassword.pack(anchor="w", padx=30, pady=(10, 0))
    self.entryPassword = ctk.CTkEntry(self, border_width=0, fg_color=theme.INPUT_COLOR, show="*",  placeholder_text="Digite sua senha")
    self.entryPassword.pack(padx=30, fill="x")
    self.entryPasswordBorder = ctk.CTkFrame(self, height=1.5, fg_color=theme.SECONDARY_COLOR)
    self.entryPasswordBorder.pack(fill="x", padx=30, pady=(0, 10))

    self.labelConfirmPassword = ctk.CTkLabel(self, text="Confirme sua senha", font=theme.LABEL_FONT, text_color=theme.PRIMARY_COLOR)
    self.labelConfirmPassword.pack(anchor="w", padx=30, pady=(10, 0))
    self.entryConfirmPassword = ctk.CTkEntry(self, border_width=0, fg_color=theme.INPUT_COLOR, show="*",  placeholder_text="Confirme sua senha")
    self.entryConfirmPassword.pack(padx=30, fill="x")
    self.entryConfirmPasswordBorder = ctk.CTkFrame(self, height=1.5, fg_color=theme.SECONDARY_COLOR)
    self.entryConfirmPasswordBorder.pack(fill="x", padx=30, pady=(0, 10))

    self.labelStatus = ctk.CTkLabel(self, text="", text_color="red")
    self.labelStatus.pack(pady=(10, 0))

    self.btnCreate = ctk.CTkButton(self, text="Alugar minhas salas", hover_color=theme.PRIMARY_COLOR_HOVER,  corner_radius=3, fg_color=theme.PRIMARY_COLOR, command=self.createAccount)
    self.btnCreate.pack(padx=30, pady=(20, 0), fill="x")

    self.frameLoginLink = ctk.CTkFrame(self, fg_color="transparent")
    self.frameLoginLink.pack(pady=(20, 0))

    self.loginText = ctk.CTkLabel(self.frameLoginLink, text="Já tem uma conta?", text_color="gray")
    self.loginText.pack(side="left")

    self.loginLink = ctk.CTkLabel(self.frameLoginLink, text=" Faça login", text_color="#4B1CFF", cursor="hand2")
    self.loginLink.pack(side="left")
    self.loginLink.bind("<Button-1>", lambda e: self.goToLoginScreen())

  def createAccount(self):
    name = self.entryName.get()
    email = self.entryEmail.get()
    cnpj = self.entryCnpj.get()
    password = self.entryPassword.get()
    confirm_password = self.entryConfirmPassword.get()

    is_valid, message = validate_admin_signup(name, email, cnpj, password, confirm_password)

    if is_valid:
      newAdmin = Admin(name, email, password, cnpj)
      saveAdmin(newAdmin)
      self.labelStatus.configure(text="Conta criada com sucesso!", text_color="green")
    else:
      self.labelStatus.configure(text=message, text_color="red")

  def goToLoginScreen(self):
    print("Navegar para tela de login...")

  def goBack(self):
    print("Voltando para tela anterior...")

