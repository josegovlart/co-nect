import customtkinter as ctk
from models.admin import Admin
from storage.persistence import saveAdmin
from styles import theme

class SignUpAdminScreen(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.title("Criar Conta - Administrador")
    self.geometry("329x665")

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("dark-blue")
    self.configure(fg_color=theme.BACKGROUND_COLOR)

    self.labelName = ctk.CTkLabel(self, text="Nome completo")
    self.labelName.pack(pady=5)
    self.entryName = ctk.CTkEntry(self, placeholder_text="Digite seu nome completo")
    self.entryName.pack()

    self.labelEmail = ctk.CTkLabel(self, text="Email")
    self.labelEmail.pack(pady=5)
    self.entryEmail = ctk.CTkEntry(self, placeholder_text="Digite seu email")
    self.entryEmail.pack()

    self.labelCnpj = ctk.CTkLabel(self, text="CNPJ")
    self.labelCnpj.pack(pady=5)
    self.entryCnpj = ctk.CTkEntry(self, placeholder_text="Digite seu CNPJ")
    self.entryCnpj.pack()

    self.labelPassword = ctk.CTkLabel(self, text="Senha")
    self.labelPassword.pack(pady=5)
    self.entryPassword = ctk.CTkEntry(self, show="*",  placeholder_text="Digite sua senha")
    self.entryPassword.pack()

    self.labelPassword = ctk.CTkLabel(self, text="Confirme sua senha")
    self.labelPassword.pack(pady=5)
    self.entryPassword = ctk.CTkEntry(self, show="*",  placeholder_text="Confirme sua senha")
    self.entryPassword.pack()

    self.btnCreate = ctk.CTkButton(self, text="Alugar minhas salas", fg_color=theme.PRIMARY_COLOR, command=self.createAccount)
    self.btnCreate.pack(pady=10)

    self.labelStatus = ctk.CTkLabel(self, text="")
    self.labelStatus.pack()

  def createAccount(self):
    name = self.entryName.get()
    email = self.entryEmail.get()
    password = self.entryPassword.get()
    cnpj = self.entryCnpj.get()

    if name and email and password and cnpj:
      newAdmin = Admin(name, email, password, cnpj)
      saveAdmin(newAdmin)
      self.labelStatus.configure(text="Conta criada com sucesso!", text_color="green")
    else:
      self.labelStatus.configure(text="Preencha todos os campos", text_color="red")
