from models.client import Client
from models.room import Room
from models.receipt import Receipt


class Reservation:
    def __init__(self, dateTime, duration, room: Room, latestReceipt: Receipt, client: Client):
        self.dateTime = dateTime
        self.duration = duration
        self.room = room
        self.latestReceipt = latestReceipt
        self.client = client

    def dataToJSON(self):
        print(self.room)
        return {
            "dateTime": self.dateTime,
            "duration": self.duration,
            "room": self.room,
            "latestReceipt": self.latestReceipt,
            "client": self.client
        }
