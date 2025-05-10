class Receipt:
    def __init__(self, type, roomId, roomName, roomAddress, price, dateTime, duration, clientName, clientEmail):
        self.type = type
        self.roomId = roomId
        self.roomName = roomName
        self.roomAddress = roomAddress
        self.price = price
        self.dateTime = dateTime
        self.duration = duration
        self.clientName = clientName
        self.clientEmail = clientEmail

    def dataToJSON(self):
        pass
