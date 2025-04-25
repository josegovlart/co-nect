from models.client import Client
from storage.persistence import saveClient, userExists
from session.auth import login
from utils.validations import validate_client_signup

class ClientController:
    @staticmethod
    def createClientAccount(name, email, password, confirm_password):
        if userExists(email):
          return False, "Já existe uma conta com esse email."
        
        is_valid, message = validate_client_signup(name, email, password, confirm_password)

        if not is_valid:
            return False, message

        new_client = Client(name, email, password)
        saveClient(new_client)
        return True, "Conta criada com sucesso!"

    @staticmethod
    def authenticateClient(email, password):
        return login(email, password)
