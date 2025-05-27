import customtkinter as ctk
from controllers.room import RoomController
from views.createReservationScreen import CreateReservationScreen
from views.reservationDetailsScreen import ReservationDetailsScreen
import tkinter as tk
from styles import theme
from session.auth import getSession
from PIL import Image, ImageTk, ImageDraw, ImageOps
from datetime import datetime, timedelta
import os

class ClientHomeScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.configure(fg_color=theme.BACKGROUND_COLOR)

        self.frameBack = ctk.CTkFrame(self, fg_color="transparent")
        self.frameBack.pack(padx=0, pady=(20, 0), anchor="w")

        self.userGreeting = ctk.StringVar()

        self.labelTitle = ctk.CTkLabel(
            self.frameBack,
            text="Co-Nect",
            text_color=theme.PRIMARY_COLOR,
            font=theme.TITLE_FONT
        )
        self.labelTitle.pack(anchor="w", padx=30, pady=(20, 10))

        self.labelGreeting = ctk.CTkLabel(
            self,
            textvariable=self.userGreeting,
            text_color=theme.TEXT_COLOR,
            font=theme.TITLE_FONT
        )
        self.labelGreeting.pack(anchor="w", padx=30, pady=(20, 10))

        self.labelReservations = ctk.CTkLabel(
            self,
            text="Minhas reservas",
            text_color=theme.TEXT_COLOR,
            font=theme.LABEL_FONT
        )
        self.labelReservations.pack(anchor="w", padx=30, pady=(20, 10))
        
        self.reservationSection = ctk.CTkFrame(self, fg_color="transparent")
        self.reservationSection.pack(fill="x", padx=20, pady=(15, 5))

        self.scrollable_frame = self.createHorizontalScrollableFrame(self.reservationSection)

        self.labelRooms = ctk.CTkLabel(
            self,
            text="Salas disponíveis",
            text_color=theme.TEXT_COLOR,
            font=theme.LABEL_FONT
        )
        self.labelRooms.pack(anchor="w", padx=30, pady=(20, 10))

        self.scrollFrame = ctk.CTkScrollableFrame(self, width=360, height=300, fg_color="white")
        self.scrollFrame.pack(padx=20, pady=5, fill="both", expand=False)

    def showRooms(self):
        for widget in self.scrollFrame.winfo_children():
            widget.destroy()

        rooms = RoomController.getAll()
        if not rooms:
            ctk.CTkLabel(self.scrollFrame, text="Você não tem salas cadastradas.", text_color=theme.TEXT_COLOR).pack()
            return
        
        for room in rooms:
            name = room.get("name", "Nome não informado")
            address = room.get("address", "Endereço não informado")
            price = f'R${room.get("price", "0")}/h'
            roomId = room.get("id")
            self.createRoomCard(self.scrollFrame, name, address, price, roomId).pack(pady=5)

    def showReservations(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        reservations = RoomController.getReservations(getSession()["email"])

        if not reservations:
            ctk.CTkLabel(self, text="Você não possui reservas.", font=("Arial", 12, "italic")).pack(pady=10)
            return

        for reservation in reservations:
            room_data = reservation["room"]
            room_name = room_data["name"]
            image_path = room_data.get("imagePath", "")
            date_time = reservation["dateTime"]
            duration = reservation["duration"]
            reservation_id = reservation["id"]

            self.createReservationCard(reservation_id, room_name, date_time, duration, image_path)

    def format_date(self, date_time_str):
        dt = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M")
        return dt.strftime("%d/%m/%Y")

    def format_hour_range(self, start_str, duration):
        dt = datetime.strptime(start_str, "%Y-%m-%d %H:%M")
        end = dt + timedelta(hours=duration)
        return f"{dt.strftime('%H:%M')} - {end.strftime('%H:%M')}"

    def onShow(self):
        self.userGreeting.set(f"Olá, {getSession()["name"]}")
        self.showRooms()
        self.showReservations()

    def handle_reservation_click(self, reservationId):
        self.controller.show_frame(ReservationDetailsScreen, reservationId=reservationId)

    def createReservation(self):
        self.controller.show_frame(CreateReservationScreen, reservationData=self.reservationData)

    def createReservationCard(self, reservation_id, name, dateTime, duration, imagePath):
        card = ctk.CTkFrame(
            self.scrollable_frame,
            corner_radius=8,
            width=150,
            height=120,
            fg_color='white',
            border_width=1,
            border_color='#e0e0e0',
        )
        card.pack(side="left", padx=5, pady=5)

        if not os.path.exists(imagePath):
            imagePath = "assets/placeholder.png"

        img = Image.open(imagePath).resize((150, 50))


        radius = 6
        mask = Image.new("L", img.size, 255)
        draw = ImageDraw.Draw(mask)
        draw.rectangle((0, radius, img.width, img.height), fill=0)
        draw.pieslice((0, 0, 2 * radius, 2 * radius), 180, 270, fill=0)
        draw.pieslice((img.width - 2 * radius, 0, img.width, 2 * radius), 270, 360, fill=0)
        draw.rectangle((radius, 0, img.width - radius, radius), fill=0)

        img.putalpha(ImageOps.invert(mask).convert("L"))
        photo = ImageTk.PhotoImage(img)

        img_container = ctk.CTkFrame(card, fg_color="transparent", width=150, height=50)
        img_container.pack(fill="x", padx=0, pady=0)

        image_label = ctk.CTkLabel(img_container, image=photo, text="")
        image_label.image = photo
        image_label.pack()

        info_frame = ctk.CTkFrame(
            card,
            fg_color="transparent",
            corner_radius=0
        )

        info_frame.pack(padx=8, pady=2, fill="both", expand=True)

        ctk.CTkLabel(
            info_frame,
            text=name,
            font=("Arial", 12, "bold"),
            anchor="w",
            justify="left"
        ).pack(fill="x", pady=(0))

        formatted_date = self.format_date(dateTime)
        hour_range = self.format_hour_range(dateTime, duration)
        
        ctk.CTkLabel(
            info_frame,
            text=formatted_date,
            font=("Arial", 11),
            anchor="w",
            justify="left"
        ).pack(anchor="w", pady=0)

        ctk.CTkLabel(
            info_frame,
            text=hour_range,
            font=("Arial", 11),
            anchor="w",
            justify="left"
        ).pack(anchor="w", pady=0)

        def on_card_click(event):
            self.handle_reservation_click(reservation_id)

        card.bind("<Button-1>", on_card_click)
        stack = [card]
        while len(stack):
            cur = stack.pop()
            for child in cur.winfo_children():
                child.configure(cursor="hand2")
                child.bind("<Button-1>", on_card_click)
                stack.append(child)

        return card

    def createRoomCard(self, parent, name, address, price, roomId):
        card = ctk.CTkFrame(parent, height=80, corner_radius=10, fg_color="#f1f1f1")
        card.pack_propagate(False)

        def on_click(e):
            self.reservationData = {
                "roomId": roomId,
                "name": name,
                "address": address,
                "price": price
            }
            self.createReservation()

        def on_enter(e):
            card.configure(fg_color="#e0e0e0")

        def on_leave(e):
            card.configure(fg_color="#f1f1f1")

        card.bind("<Button-1>", on_click)
        card.bind("<Enter>", on_enter)
        card.bind("<Leave>", on_leave)

        row = ctk.CTkFrame(card, fg_color="transparent")
        row.pack(fill="x", padx=5, pady=5)

        img = Image.open("assets/placeholder.png").resize((150, 50))
        img = ctk.CTkImage(light_image=img, size=(50, 50))
        img_label = ctk.CTkLabel(row, image=img, text="")
        img_label.pack(side="left", padx=5)

        info = ctk.CTkFrame(row, fg_color="transparent")
        info.pack(side="left", fill="both", expand=True)

        name_label = ctk.CTkLabel(info, text=name, font=("Helvetica", 12, "bold"))
        name_label.pack(anchor="w")

        address_label = ctk.CTkLabel(info, text=address, font=("Helvetica", 10))
        address_label.pack(anchor="w")

        price_label = ctk.CTkLabel(info, text=price, font=("Helvetica", 10, "italic"))
        price_label.pack(anchor="w")

        for child in [row, img_label, info, name_label, address_label, price_label]:
            child.bind("<Button-1>", on_click)
            child.bind("<Enter>", on_enter)
            child.bind("<Leave>", on_leave)
            child.configure(cursor="hand2")

        return card

    def createHorizontalScrollableFrame(self, parent):
        canvas = tk.Canvas(parent, height=150, bg="white", highlightthickness=0)
        scrollbar = tk.Scrollbar(parent, orient="horizontal", command=canvas.xview)
        scrollable_frame = ctk.CTkFrame(canvas, fg_color=theme.BACKGROUND_COLOR)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(xscrollcommand=scrollbar.set)

        canvas.pack(side="top", fill="x", expand=False)
        scrollbar.pack(side="bottom", fill="x")

        return scrollable_frame
