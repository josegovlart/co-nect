import customtkinter as ctk
from components.roomCard import RoomCard
from controllers.room import RoomController
from views.createRoomScreen import CreateRoomScreen
from styles import theme
from session.auth import getSession

class AdminHomeScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.userGreeting = ctk.StringVar()

        self.configure(fg_color=theme.BACKGROUND_COLOR)

        self.mainLayout = ctk.CTkFrame(self, fg_color="transparent")
        self.mainLayout.pack(fill="both", expand=True, padx=30, pady=30)

        self.labelTitle = ctk.CTkLabel(
            self.mainLayout,
            text="Co-Nect",
            text_color=theme.PRIMARY_COLOR,
            font=theme.TITLE_FONT
        )
        self.labelTitle.pack(anchor="w", pady=(0, 10))

        self.labelSpaces = ctk.CTkLabel(
            self.mainLayout,
            text="Meus espaços",
            text_color=theme.TEXT_COLOR,
            font=theme.LABEL_FONT
        )
        self.labelSpaces.pack(anchor="w", pady=(0, 10))

        self.scrollFrame = ctk.CTkScrollableFrame(
            self.mainLayout,
            fg_color="transparent",
            height=380
        )
        self.scrollFrame.pack(fill="both", expand=False)

        self.btnCreate = ctk.CTkButton(
            self.mainLayout,
            text="Adicionar espaço",
            hover_color=theme.PRIMARY_COLOR_HOVER,
            corner_radius=6,
            fg_color=theme.PRIMARY_COLOR,
            command=self.goToCreateRoom
        )
        self.btnCreate.pack(pady=(20, 10), fill="x")

        self.btnReports = ctk.CTkButton(
            self.mainLayout,
            text="Ver relatórios",
            hover_color=theme.TRANSPARENT_HOVER,
            text_color=theme.PRIMARY_COLOR,
            corner_radius=6,
            fg_color=theme.BACKGROUND_COLOR,
            command=self.goToReports
        )
        self.btnReports.pack(pady=(0, 10), fill="x")

    def showRooms(self):
        for widget in self.scrollFrame.winfo_children():
            widget.destroy()

        rooms = RoomController.getRoomsByAdminEmail(getSession()["email"])
        if not rooms:
            ctk.CTkLabel(self.scrollFrame, text="Você não tem salas cadastradas.", text_color=theme.TEXT_COLOR).pack()
            return

        for room in rooms:
            card = RoomCard(self.scrollFrame, room, self.controller)
            card.pack(padx=0, pady=10, fill="x")

    def onShow(self):
        self.showRooms()

    def goToCreateRoom(self):
        self.controller.show_frame(CreateRoomScreen)

    def goToReports(self):
        print("Bora ver esses relatórios")
