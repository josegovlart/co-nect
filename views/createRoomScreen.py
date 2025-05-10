import customtkinter as ctk
from controllers.client import ClientController
from controllers.room import RoomController
from session.auth import getSession
from styles import theme


class CreateRoomScreen(ctk.CTkFrame):
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

        self.labelSpaces = ctk.CTkLabel(
            self,
            text="Criar espaço",
            text_color=theme.TEXT_COLOR,
            font=theme.LABEL_FONT
        )
        self.labelSpaces.pack(anchor="w", padx=30, pady=(20, 10))

        self.entryName = self.createInput("Nome da sala", "Digite o nome da sala")
        self.entryAddress = self.createInput("Endereço", "Endereço da sala")
        self.entryDescription = self.createInput("Descrição", "Descrição do espaço")
        self.entryPrice = self.createInput("Preço por hora", "Preço por hora")

        self.labelStatus = ctk.CTkLabel(self, text="", text_color="red")
        self.labelStatus.pack(pady=(10, 0))

        self.btnCreate = ctk.CTkButton(
            self,
            text="Criar espaço",
            hover_color=theme.PRIMARY_COLOR_HOVER,
            corner_radius=3,
            fg_color=theme.PRIMARY_COLOR,
            command=self.createRoom
        )
        self.btnCreate.pack(padx=30, pady=(20, 0), fill="x")

    def createRoom(self):
        name = self.entryName.get()
        address = self.entryAddress.get()
        description = self.entryDescription.get()
        price = self.entryPrice.get()

        success, message = RoomController.createRoom(name, address, description, price, getSession()["email"])

        if success:
            self.labelStatus.configure(text=message, text_color="green")

            def clearFields():
                self.entryName.delete(0, "end")
                self.entryAddress.delete(0, "end")
                self.entryDescription.delete(0, "end")
                self.entryPrice.delete(0, "end")
                self.labelStatus.configure(text="")

            self.after(1000, self.goBack)
            self.after(1000, clearFields)
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

    def goBack(self):
        from views.adminHomeScreen import AdminHomeScreen
        self.controller.show_frame(AdminHomeScreen)
