from models.user import User

class Client(User):
  def __init__(self, cardNumber, expireDate, cardHolder):
    self.cardNumber = cardNumber
    self.expireDate = expireDate,
    self.cardHolder = cardHolder,

  def dataToJSON(self):
    pass
