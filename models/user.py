from abc import ABC, abstractmethod

class User(ABC):
  def __init__(self, name, email, password, profilePicture=None):
    self.name = name
    self.email = email
    self.password = password
    self.profilePicture = profilePicture
  
  @abstractmethod
  def dataToJSON(self):
    pass
