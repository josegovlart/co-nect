from models.user import User
import bcrypt

class Admin(User):
  def __init__(self, name, email, password, cnpj, profilePicture=None):
    super().__init__(name, email, password, profilePicture)
    self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    self.cnpj = cnpj
    self.rooms = []

  def dataToJSON(self):
    return {
      "type": "admin",
      "name": self.name,
      "email": self.email,
      "password": self.password,
      "profilePicture": self.profilePicture,
      "cnpj": self.cnpj,
      "rooms": self.rooms
    }
