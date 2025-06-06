from models.user import User

class CreditCard(User):
    def __init__(self, cardNumber, expireDate, cardHolder):
        self.cardNumber = cardNumber
        self.expireDate = expireDate
        self.cardHolder = cardHolder

    def dataToJSON(self):
        return {
            "cardNumber": self.cardNumber,
            "expireDate": self.expireDate,
            "cardHolder": self.cardHolder
        }
