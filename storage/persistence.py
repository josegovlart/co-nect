import json
import os

DATA_FILE_PATH = "storage/data.json"

def loadData():
  if os.path.exists(DATA_FILE_PATH):
     with open(DATA_FILE_PATH, "r") as f:
            return json.load(f)
  return {"admins": []}

def saveAdmin(admin):
    dados = loadData()
    dados["admins"].append(admin.dataToJSON())
    with open(DATA_FILE_PATH, "w") as f:
      json.dump(dados, f, indent=2)
