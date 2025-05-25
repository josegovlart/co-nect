import customtkinter as ctk
from PIL import Image
import qrcode


class PaymentPopup(ctk.CTkToplevel):
    def __init__(self, parent, dateTime, duration, room, latestReceipt, confirm_callback):
        super().__init__(parent)
        self.title("Pagamento")
        self.geometry("420x520")
        self.resizable(False, False)
        self.grab_set()

        self.dateTime = dateTime
        self.duration = duration
        self.room = room
        self.latestReceipt = latestReceipt
        self.confirm_callback = confirm_callback

        self.payment_method = ctk.StringVar(value="Pix")

        self.content_frame = None

        self.configure(fg_color="#FFFFFF")

        self.build_interface()

    def build_interface(self):
        ctk.CTkLabel(self, text="Selecione o método de pagamento", font=("Arial", 18, "bold"),
                     text_color="#000000").pack(pady=(20, 10))

        option_frame = ctk.CTkFrame(self, fg_color="#F5F5F5", corner_radius=15)
        option_frame.pack(pady=10)

        ctk.CTkRadioButton(option_frame, text="Pix", variable=self.payment_method, value="Pix",
                            command=self.update_content, fg_color="#7A50F5", border_color="#7A50F5").pack(side="left", padx=15, pady=10)

        ctk.CTkRadioButton(option_frame, text="Cartão", variable=self.payment_method, value="Card",
                            command=self.update_content, fg_color="#7A50F5", border_color="#7A50F5").pack(side="left", padx=15, pady=10)

        self.content_frame = ctk.CTkFrame(self, fg_color="#FFFFFF")
        self.content_frame.pack(pady=10, fill="both", expand=True)

        self.update_content()

        button_frame = ctk.CTkFrame(self, fg_color="#FFFFFF")
        button_frame.pack(pady=10)

        ctk.CTkButton(button_frame, text="Voltar", fg_color="#FFFFFF", border_color="#7A50F5",
                       border_width=2, text_color="#7A50F5", hover_color="#E0D8FC", command=self.destroy).pack(side="left", padx=10)

        ctk.CTkButton(button_frame, text="Pagar", fg_color="#7A50F5", hover_color="#6A3DE9",
                       text_color="#FFFFFF", command=self.pay).pack(side="left", padx=10)

    def update_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        if self.payment_method.get() == "Pix":
            self.render_pix()
        else:
            self.render_card()

    def render_pix(self):
        ctk.CTkLabel(self.content_frame, text="Escaneie o QR Code abaixo", font=("Arial", 14, "bold"),
                     text_color="#000000").pack(pady=10)

        qr_data = f"Pagamento para reserva em {self.dateTime} - Sala {self.room['name']}"
        qr = qrcode.make(qr_data)
        qr = qr.resize((200, 200))

        qr_img = ctk.CTkImage(light_image=qr, dark_image=qr, size=(200, 200))

        ctk.CTkLabel(self.content_frame, image=qr_img, text="").pack(pady=10)

        ctk.CTkButton(self.content_frame, text="Esperando pagamento", state="disabled",
                      fg_color="#E0D8FC", text_color="#7A50F5", corner_radius=10).pack(pady=10)

    def render_card(self):
        ctk.CTkLabel(self.content_frame, text="Selecione um cartão", font=("Arial", 14, "bold"),
                     text_color="#000000").pack(pady=10)

        card_frame = ctk.CTkFrame(self.content_frame, fg_color="#F5F5F5", corner_radius=15)
        card_frame.pack(pady=5, padx=20, fill="x")

        ctk.CTkLabel(card_frame, text="💳 2433 4213 4985 312  - 07/2028", text_color="#000000").pack(pady=5)

        ctk.CTkButton(self.content_frame, text="Adicionar cartão", fg_color="#FFFFFF", border_color="#7A50F5",
                      border_width=2, text_color="#7A50F5", hover_color="#E0D8FC",
                      command=self.render_add_card).pack(pady=8)

    def render_add_card(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        ctk.CTkLabel(self.content_frame, text="Adicione um cartão", font=("Arial", 14, "bold"),
                     text_color="#000000").pack(pady=10)

        # Cartão exemplo
        card_frame = ctk.CTkFrame(self.content_frame, fg_color="#F5F5F5", corner_radius=15)
        card_frame.pack(pady=5, padx=20, fill="x")

        ctk.CTkLabel(card_frame, text="💳 2433 4213 4985 312  - 07/2028", text_color="#000000").pack(pady=5)

        form_frame = ctk.CTkFrame(self.content_frame, fg_color="#FFFFFF")
        form_frame.pack(pady=5)

        ctk.CTkEntry(form_frame, placeholder_text="Número do cartão", width=300).pack(pady=5)
        ctk.CTkEntry(form_frame, placeholder_text="Data de vencimento (MM/AA)", width=300).pack(pady=5)
        ctk.CTkEntry(form_frame, placeholder_text="Nome do portador", width=300).pack(pady=5)

        button_frame = ctk.CTkFrame(self.content_frame, fg_color="#FFFFFF")
        button_frame.pack(pady=10)

        ctk.CTkButton(button_frame, text="Voltar", fg_color="#FFFFFF", border_color="#7A50F5",
                       border_width=2, text_color="#7A50F5", hover_color="#E0D8FC",
                       command=self.update_content).pack(side="left", padx=10)

        ctk.CTkButton(button_frame, text="Adicionar cartão", fg_color="#7A50F5", hover_color="#6A3DE9",
                       text_color="#FFFFFF", command=self.update_content).pack(side="left", padx=10)

    def pay(self):
        self.confirm_callback(self.dateTime, self.duration, self.latestReceipt)
        self.destroy()
