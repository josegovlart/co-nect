import uuid
from models.room import Room
from storage.persistence import saveRoom, getRooms
from utils.validations import validate_room_create


class RoomController:
    @staticmethod
    def createRoom(name, address, description, price, adminEmail):
        is_valid, message = validate_room_create(name, address, description, price)

        if not is_valid:
            return False, message

        room_id = str(uuid.uuid4())
        price = price.replace(",", ".")
        price_float = float(price)
        new_room = Room(room_id, name, address, description, price_float, adminEmail)
        saveRoom(new_room)
        return True, "Sala criada com sucesso!"

    @staticmethod
    def getRoomsByAdminEmail(admin_email):
        return getRooms(admin_email)

    @staticmethod
    def getRoomById(room_id):
        pass

    @staticmethod
    def deleteRoomById(room_id):
        pass

    @staticmethod
    def editRoomById(room_id, name, address, description, price):
        is_valid, message = validate_room_create(name, address, description, price)

        if not is_valid:
            return False, message

        pass