import json
from transaction import Transaction

FILE_PATH = "data.json"

def load_data():
    try:
        with open(FILE_PATH, "r") as f:
            data = json.load(f)
            return {user: {"name": info["name"], "password": info["password"], 
                           "transactions": [Transaction.from_dict(t) for t in info["transaction"]]} 
                    for user, info in data.items()}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data):
    with open(FILE_PATH, "w") as f:
        json.dump({user: {"name": info["name"], "password": info["password"], 
                          "transaction": [t.to_dict() for t in info["transactions"]]} 
                   for user, info in data.items()}, f, indent=4)