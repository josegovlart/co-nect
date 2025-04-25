from models.admin import Admin
from storage.persistence import saveAdmin, userExists
from session.auth import login
from utils.validations import validate_admin_signup

class AdminController:
    @staticmethod
    def createAdminAccount(name, email, cnpj, password, confirm_password):
        if userExists(email):
          return False, "Já existe uma conta com esse email."
        
        is_valid, message = validate_admin_signup(name, email, cnpj, password, confirm_password)

        if not is_valid:
            return False, message

        new_admin = Admin(name, email, password, cnpj)
        saveAdmin(new_admin)
        return True, "Conta criada com sucesso!"

    @staticmethod
    def authenticateAdmin(email, password):
        return login(email, password)
