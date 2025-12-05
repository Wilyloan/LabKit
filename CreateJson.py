import json
import os

documents_folder = os.path.join(os.path.expanduser('~'), "Documents")
os.makedirs(documents_folder, exist_ok=True)
FILE_PATH = os.path.join(documents_folder, "password.json")

def save_json(data: dict):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def set_password(site: str, login: str, password: str):
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
    else:
        data = {}

    if site not in data:
        data[site] = []

    data[site].append({"login": login, "password": password})

    save_json(data)


def delete_account(site: str, login: str = None):
    if not os.path.exists(FILE_PATH):
        return FileNotFoundError
    
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return ConnectionError
    
    if site not in data:
        return KeyError
    
    if login is None:
        del data[site]
    else:
        original_len = len(data[site])
        data[site] = [acc for acc in data[site] if acc["login"] != login]
        if not data[site]:
            del data[site]
    
    save_json(data)

    

def load_json():
        if not os.path.exists(FILE_PATH):
            data = {}
        else:
            try:
                with open(FILE_PATH, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except json.JSONDecodeError:
                data = {}
        return data