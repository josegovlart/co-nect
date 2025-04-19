from models.user import User

class Admin(User):
  def __init__(self, name, email, password, cnpj, profilePicture=None):
    super().__init__(name, email, password, profilePicture)
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
