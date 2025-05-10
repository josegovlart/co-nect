import json
import os

DATA_FILE_PATH = "storage/data.json"

def loadData():
    if os.path.exists(DATA_FILE_PATH):
        try:
            with open(DATA_FILE_PATH, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {"admins": [], "clients": [], "rooms": []}
    return {"admins": [], "clients": [], "rooms": []}

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

def saveRoom(room):
    dados = loadData()
    dados["rooms"].append(room.dataToJSON())
    with open(DATA_FILE_PATH, "w") as f:
        json.dump(dados, f, indent=2)

def getRooms(email):
    data = loadData()
    result = []
    for room in data["rooms"]:
        if room["adminEmail"] == email:
            result.append(room)

    return result

def editRoom(newData):
    dados = loadData()
    for room in dados["rooms"]:
        if room["id"] == newData.room_id:
            if newData.adminEmail != room["adminEmail"]:
                return False, "Você não tem permissão para editar."
            room["name"] = newData.name
            room["address"] = newData.address
            room["description"] = newData.description
            room["price"] = newData.price
            break
    else:
        return False, "Sala não encontrada."

    with open(DATA_FILE_PATH, "w") as f:
        json.dump(dados, f, indent=2)

    return True, "Sala atualizada com sucesso!"

def deleteRoom(roomId, adminEmail):
    dados = loadData()
    for i, room in enumerate(dados["rooms"]):
        if room["id"] == roomId:
            if room["adminEmail"] != adminEmail:
                return False, "Você não tem permissão para deletar esta sala."

            del dados["rooms"][i]
            with open(DATA_FILE_PATH, "w") as f:
                json.dump(dados, f, indent=2)

            return True, "Sala deletada com sucesso."

    return False, "Sala não encontrada."