import re
from datetime import datetime, timedelta

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

def validate_client_signup(name, email, password, confirm_password):
    if not all([name, email, password, confirm_password]):
        return False, "Todos os campos são obrigatórios."
    if not is_valid_email(email):
        return False, "Email inválido."
    if not is_strong_password(password):
        return False, "A senha deve ter pelo menos 6 caracteres."
    if password != confirm_password:
        return False, "As senhas não coincidem."
    return True, ""

def validate_room_create(name, address, description, price):
    if not all([name, address, description, price]):
        return False, "Todos os campos são obrigatórios."

    pattern = r"^\d{1,5}(,\d{2})?$"
    if not re.match(pattern, price):
        return False, "O preço por hora deve estar no formato dd,dd (ex: 50,00)."

    return True, ""

def validate_reservation_fields(date, time):
    if not all([date, time]):
        return False, "Todos os campos são obrigatórios."

    return True, ""

def is_time_conflict(existing_start, existing_duration, new_start, new_duration):
    fmt = "%Y-%m-%d %H:%M"
    e_start = datetime.strptime(existing_start, fmt)
    n_start = datetime.strptime(new_start, fmt)

    existing_duration = int(existing_duration)
    new_duration = int(new_duration)

    e_end = e_start + timedelta(hours=existing_duration)
    n_end = n_start + timedelta(hours=new_duration)

    return not (n_end <= e_start or n_start >= e_end)

def validate_blank_fields(fields):
    return all(fields)

def is_valid_date_format(date):
    try:
        datetime.strptime(date, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def is_valid_time_format(time):
    try:
        datetime.strptime(time, "%H:%M")
        return True
    except ValueError:
        return False

def is_after_now(dateTime):
    dt = datetime.strptime(dateTime, "%d/%m/%Y %H:%M")
    return dt > datetime.now()
