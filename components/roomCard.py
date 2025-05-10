import customtkinter as ctk
from PIL import Image
from styles import theme

class RoomCard(ctk.CTkFrame):
    def __init__(self, parent, room_data):
        super().__init__(parent, fg_color=theme.INPUT_COLOR, corner_radius=12)

        content = ctk.CTkFrame(self, fg_color="transparent")
        content.pack(fill="x", padx=0, pady=0)

        try:
            image_path = room_data.get("image_path", "assets/placeholder.png")
            image = ctk.CTkImage(light_image=Image.open(image_path), size=(60, 60))
        except Exception:
            image = None

        if image:
            image_label = ctk.CTkLabel(content, image=image, text="")
            image_label.pack(side="left", padx=0)

        info_frame = ctk.CTkFrame(content, fg_color="transparent")
        info_frame.pack(side="left", expand=True)

        ctk.CTkLabel(info_frame, text=room_data["name"], font=theme.CARD_TITLE_FONT, text_color=theme.TEXT_COLOR).pack(anchor="w")
        ctk.CTkLabel(info_frame, text=room_data["address"], font=theme.DESCRIPTION_FONT, text_color="#797979").pack(anchor="w")
        ctk.CTkLabel(info_frame, text=f"R$ {room_data['price']:.2f}/h", font=theme.DESCRIPTION_FONT, text_color=theme.TEXT_COLOR).pack(anchor="w", pady=(2, 0))

        action_frame = ctk.CTkFrame(content, fg_color="transparent")
        action_frame.pack(side="right", padx=(15, 0))

        calendar_icon = ctk.CTkButton(action_frame, text="📅", width=30, height=30, fg_color="transparent", hover_color=theme.TRANSPARENT_HOVER, command=self.edit_room)
        calendar_icon.pack(pady=2)

        trash_icon = ctk.CTkButton(action_frame, text="🗑️", width=30, height=30, fg_color="transparent", hover_color=theme.TRANSPARENT_HOVER, command=self.delete_room)
        trash_icon.pack(pady=2)

    def edit_room(self):
        print("Editar Sala")

    def delete_room(self):
        print("Deletar sala")