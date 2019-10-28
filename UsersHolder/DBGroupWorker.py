import json


def set_user_group(chat_id_int: int, group: str):
    chat_id = str(chat_id_int)
    data = read_users_json()
    data[chat_id] = group
    save_users_json(data)


def get_user_group(chat_id_int: int):
    chat_id = str(chat_id_int)
    return read_users_json()[chat_id]


def read_users_json() -> dict:
    data = {}
    with open('Data/Users.json') as json_file:
        data = json.load(json_file)
    return data


def save_users_json(data):
    with open('Data/Users.json', 'w') as outfile:
        json.dump(data, outfile)
