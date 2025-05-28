from storage.persistence import saveCreditCard, getCreditCard

class CreditCardController:
    @staticmethod
    def addOrUpdateCard(email, cardNumber, expireDate, cardHolder):
        saveCreditCard(email, cardNumber, expireDate, cardHolder)

    @staticmethod
    def getCard(email):
        return getCreditCard(email)
