import json
import os

DATA_FILE_PATH = "storage/data.json"

def loadData():
    if os.path.exists(DATA_FILE_PATH):
        try:
            with open(DATA_FILE_PATH, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {"admins": [], "clients": []}
    return {"admins": [], "clients": []}

def saveAdmin(admin):
    dados = loadData()
    dados["admins"].append(admin.dataToJSON())
    with open(DATA_FILE_PATH, "w") as f:
        json.dump(dados, f, indent=2)

def saveClient(clients):
    dados = loadData()
    dados["clients"].append(clients.dataToJSON())
    with open(DATA_FILE_PATH, "w") as f:
      json.dump(dados, f, indent=2)

def getUserJSON(email):
    data = loadData()
    for client in data["clients"]:
        if (client["email"] == email):
            return True, client
    for admin in data["admins"]:
        if (admin["email"] == email):
            return True, admin
    return False, None

def userExists(email):
    exists, _ = getUserJSON(email)
    return exists
