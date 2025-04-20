
import re

def is_valid_email(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

def is_valid_cnpj(cnpj):
    cnpj = re.sub(r'\D', '', cnpj)
    return len(cnpj) == 14 and cnpj.isdigit()

def is_strong_password(password):
    return len(password) >= 6

def validate_admin_signup(name, email, cnpj, password, confirm_password):
    if not all([name, email, cnpj, password, confirm_password]):
        return False, "Todos os campos são obrigatórios."
    if not is_valid_email(email):
        return False, "Email inválido."
    if not is_valid_cnpj(cnpj):
        return False, "CNPJ inválido."
    if not is_strong_password(password):
        return False, "A senha deve ter pelo menos 6 caracteres."
    if password != confirm_password:
        return False, "As senhas não coincidem."
    return True, ""
