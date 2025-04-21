from models.user import User
import bcrypt

class Client(User):
  def __init__(self, name, email, password, profilePicture=None, creditCard=None):
    super().__init__(name, email, password, profilePicture)
    self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    self.creditCard = creditCard
    self.reservations = []

  def dataToJSON(self):
    return {
      "type": "client",
      "name": self.name,
      "email": self.email,
      "password": self.password,
      "profilePicture": self.profilePicture,
      "creditCard": self.creditCard,
      "reservations": self.reservations
    }
