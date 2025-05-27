import uuid
from models.reservation import Reservation
from storage.persistence import saveReservation, getReservationsByRoom, getRoomById, getUserJSON, getReservationById, erase_reservation_by_id, append_raw_json
from utils.validations import is_time_conflict, validate_blank_fields, is_valid_date_format, is_valid_time_format, is_after_now
import datetime

class ReservationController:
    @staticmethod
    def is_room_available(room_id, new_start, new_duration, reservation_id=None):
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
        if not ReservationController.is_room_available(room["id"], dateTime, duration):
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

    @staticmethod
    def reschedule_reservation(reservation_id, date, time):
        fields_filled = validate_blank_fields([reservation_id, date, time])
        if fields_filled:
            date_valid = is_valid_date_format(date)
            if date_valid:
                time_valid = is_valid_time_format(time)
                if time_valid:
                    after_now = is_after_now(date + " " + time)
                    if after_now:
                        reservation = getReservationById(reservation_id)
                        current_duration = reservation["duration"]
                        room_id = reservation["room"]["id"]
                        dt = datetime.datetime.strptime(date + " " + time, "%d/%m/%Y %H:%M")
                        formatted = dt.strftime("%Y-%m-%d %H:%M")
                        available = ReservationController.is_room_available(room_id, formatted, current_duration, reservation_id)
                        if available:
                            ReservationController.update_reservation_date(reservation_id, date, time)
                            return True, "Reserva remarcada com sucesso."
                        else:
                            return False, "O horário escolhido não está disponível. Escolha outro horário ou outra data."
                    else:
                        return False, "A data e o horário escolhidos devem ser após o dia atual."
                else:
                    return False, "Horário inválido: Use o formato HH:MM."
            else:
                return False, "Data inválida. Use o formato DD/MM/AAAA."
        else:
            return False, "Todos os campos são obrigatórios."

    @staticmethod
    def update_reservation_date(reservation_id, date, time):
        reservation = getReservationById(reservation_id)
        erase_reservation_by_id(reservation_id)
        dt_str = date + " " + time
        dt = datetime.datetime.strptime(dt_str, "%d/%m/%Y %H:%M")
        formatted = dt.strftime("%Y-%m-%d %H:%M")
        reservation["dateTime"] = formatted
        append_raw_json("reservations", reservation)

