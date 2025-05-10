from models.client import Client
from models.room import Room
from models.receipt import Receipt


class Reservation:
    def __init__(self, dateTime, duration, room: Room, latestReceiption: Receipt, client: Client):
        self.dateTime = dateTime
        self.duration = duration
        self.room = room
        self.latestReceiption = latestReceiption
        self.client = client

    def dataToJSON(self):
        pass
