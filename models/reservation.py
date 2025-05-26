from models.client import Client
from models.room import Room
from models.receipt import Receipt


class Reservation:
    def __init__(self, reservation_id, dateTime, duration, room: Room, latestReceipt: Receipt, client: Client):
        self.reservation_id = reservation_id
        self.dateTime = dateTime
        self.duration = duration
        self.room = room
        self.latestReceipt = latestReceipt
        self.client = client

    def dataToJSON(self):
        return {
            "id": self.reservation_id,
            "dateTime": self.dateTime,
            "duration": self.duration,
            "room": self.room,
            "latestReceipt": self.latestReceipt,
            "client": self.client
        }
