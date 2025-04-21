from storage.persistence import getUserJSON
import bcrypt
import json
import os

SESSION_FILE_PATH = "session/session.json"


def getSession():
    if os.path.exists(SESSION_FILE_PATH):
        with open(SESSION_FILE_PATH, "r") as f:
            return json.load(f)
    return {}


def setSession(name, email, profilePicture):
    data = {
        "name": name,
        "email": email,
        "profilePicture": profilePicture
    }
    with open(SESSION_FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)


def login(email, password):
    success, user = getUserJSON(email)
    if success and bcrypt.checkpw(password.encode('utf-8'), user["password"].encode('utf-8')):
        setSession(user["name"], user["email"], user["profilePicture"])
        return True, "Usuário autenticado com sucesso.", user["type"]
    return False, "Email ou senha incorretos."
