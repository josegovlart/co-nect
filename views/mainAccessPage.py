import customtkinter as ctk
from PIL import Image
from styles import theme
from views.createRoomScreen import CreateRoomScreen
from views.createReservationScreen import CreateReservationScreen
from views.editRoomScreen import EditRoomScreen
from views.signUpAdminScreen import SignUpAdminScreen
from views.signUpClientScreen import SignUpClientScreen
from views.loginScreen import LoginScreen
from views.clientHomeScreen import ClientHomeScreen
from views.adminHomeScreen import AdminHomeScreen

class MainAccessPage(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Co-nect")
        self.geometry("329x665")

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")
        self.configure(fg_color=theme.BACKGROUND_COLOR)

        self.main_frame = ctk.CTkFrame(self, fg_color=theme.BACKGROUND_COLOR)
        self.main_frame.place(relwidth=1, relheight=1)

        self.logo_image = ctk.CTkImage(
            light_image=Image.open("assets/main_image.png"),
            size=(330, 400)
        )
        self.logoLabel = ctk.CTkLabel(self.main_frame, image=self.logo_image, text="")
        self.logoLabel.pack(pady=(0, 10))

        self.labelStatus = ctk.CTkLabel(self.main_frame, text="", text_color="red")
        self.labelStatus.pack(pady=(10, 0))

        # Botão Entrar
        self.btnJoin = ctk.CTkButton(
            self.main_frame,
            text="Entrar",
            hover_color=theme.PRIMARY_COLOR_HOVER,
            corner_radius=3,
            fg_color=theme.PRIMARY_COLOR
        )
        self.btnJoin.pack(padx=30, pady=(20, 0), fill="x")
        self.btnJoin.bind("<Button-1>", lambda e: self.goToLoginScreen())

        # Botão Quero reservar salas
        self.btnReserve = ctk.CTkButton(
            self.main_frame,
            text="Quero reservar salas",
            text_color=theme.PRIMARY_COLOR,
            hover_color=theme.TRANSPARENT_HOVER,
            corner_radius=3,
            fg_color=theme.BACKGROUND_COLOR,
            border_color=theme.PRIMARY_COLOR,
            border_width=2
        )
        self.btnReserve.pack(padx=30, pady=(20, 0), fill="x")
        self.btnReserve.bind("<Button-1>", lambda e: self.goToUserSignUpScreen())

        self.frameLoginLink = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.frameLoginLink.pack(pady=(20, 0))

        # Botão Sou dono de coworking
        self.adminSignUpLink = ctk.CTkLabel(
            self.frameLoginLink,
            text="Sou dono de coworking",
            text_color="#4B1CFF",
            cursor="hand2"
        )
        self.adminSignUpLink.pack(side="left")
        self.adminSignUpLink.bind("<Button-1>", lambda e: self.goToAdminSignUpScreen())

        self.frames = {}
        for F in (SignUpAdminScreen,
                  SignUpClientScreen,
                  LoginScreen,
                  ClientHomeScreen,
                  AdminHomeScreen,
                  CreateRoomScreen,
                  CreateReservationScreen,
                  EditRoomScreen):
            frame = F(parent=self, controller=self)
            self.frames[F] = frame
            frame.place(relwidth=1, relheight=1)
            frame.place_forget()

        self.show_frame(MainAccessPage)

    def show_frame(self, frame_class, **kwargs):
        for frame in self.frames.values():
            frame.place_forget()

        if frame_class == self.__class__:
            self.main_frame.place(relwidth=1, relheight=1)
        else:
            self.main_frame.place_forget()
            frame = self.frames[frame_class]

            if hasattr(frame, "set_data") and kwargs:
                frame.set_data(**kwargs)

            frame.place(relwidth=1, relheight=1)

            if hasattr(frame, "onShow"):
                frame.onShow()

    def goToLoginScreen(self):
        self.show_frame(LoginScreen)

    def goToAdminSignUpScreen(self):
        self.show_frame(SignUpAdminScreen)

    def goToUserSignUpScreen(self):
        self.show_frame(SignUpClientScreen)
