class Room:
    def __init__(self, room_id, name, address, description, price, adminEmail):
        self.room_id = room_id
        self.name = name
        self.address = address
        self.description = description
        self.price = price
        self.adminEmail = adminEmail

    def dataToJSON(self):
        return {
            "id": self.room_id,
            "name": self.name,
            "address": self.address,
            "description": self.description,
            "price": self.price,
            "adminEmail": self.adminEmail,
        }
