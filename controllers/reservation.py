import uuid
from models.reservation import Reservation
from storage.persistence import saveReservation, getReservationsByRoom, getRoomById, getUserJSON, getReservationById
from utils.validations import is_time_conflict, validate_reservation_fields

class ReservationController:
    @staticmethod
    def isRoomAvailable(room_id, new_start, new_duration, reservation_id=None):
        # Validação de tipos
        if isinstance(new_duration, str):
            try:
                new_duration = int(new_duration)
            except ValueError:
                raise ValueError("Duração deve ser um número (ex: 2) ou string convertível (ex: '2')")
        
        reservations = getReservationsByRoom(room_id)

        for r in reservations:
            existing_start = r["dateTime"]
            existing_duration = r["duration"]
            
            if is_time_conflict(existing_start, existing_duration, new_start, new_duration) and r["id"] != reservation_id:
                return False
        return True

    @staticmethod
    def reserveRoom(dateTime, duration, room, latestReceipt, client):
        if not ReservationController.isRoomAvailable(room["id"], dateTime, duration):
            return False, "Sala já reservada nesse horário."

        reservation_id = str(uuid.uuid4())
        reservation = Reservation(reservation_id, dateTime, duration, room, latestReceipt, client)
        saveReservation(reservation)
        return True, "Reserva realizada com sucesso!"
    
    @staticmethod
    def getReservationRoomById(room_id):
        return getRoomById(room_id)
    
    @staticmethod
    def clientData(email):
        return getUserJSON(email)

    @staticmethod
    def getReservationById(reservation_id):
        return getReservationById(reservation_id)
