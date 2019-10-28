import json


def get_names(group: str):
    data = {}
    with open('Data/NamesOfTeachers.json') as json_file:
        data = json.load(json_file)
    return data["names"][str(group)]