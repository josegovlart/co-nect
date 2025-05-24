import uuid
from models.room import Room
from storage.persistence import saveRoom, getRooms, editRoom, deleteRoom, getAllRooms, getReservationsByClient
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
    def getReservations(client_email):
        return getReservationsByClient(client_email)

    @staticmethod
    def getAll():
        return getAllRooms()

    @staticmethod
    def getRoomById(room_id):
        pass

    @staticmethod
    def deleteRoomById(room_id, adminEmail):
        is_valid, message = deleteRoom(room_id, adminEmail)

        if not is_valid:
            return False, message

        return True, "Sala deletada com sucesso!"

    @staticmethod
    def editRoomById(room_id, name, address, description, price, adminEmail):
        is_valid, message = validate_room_create(name, address, description, price)

        if not is_valid:
            return False, message

        price = price.replace(",", ".")
        price_float = float(price)
        new_room = Room(room_id, name, address, description, price_float, adminEmail)
        editRoom(new_room)

        return True, "Sala editada com sucesso!"
