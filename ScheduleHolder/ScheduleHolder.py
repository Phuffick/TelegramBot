import json
from datetime import date


def get_schedule_today(group: str):
    weekday = date.today().weekday()
    if weekday > 4:
        return None
    else:
        return get_schedule(group, weekday)


def get_schedule_next(group: str):
    weekday = date.today().weekday()
    weekday += 1
    if weekday > 4:
        weekday = 0
    return get_schedule(group, weekday)


def get_times():
    data = {}
    with open('Data/ScheduleList.json') as json_file:
        data = json.load(json_file)
    return data['times']


def get_schedule(group: str, day: int):
    data = {}
    with open('Data/ScheduleList.json') as json_file:
        data = json.load(json_file)
    return data['schedules'][group][str(day)]


def get_all_schedule(group: str):
    data = {}
    with open('Data/ScheduleList.json') as json_file:
        data = json.load(json_file)
    return data['schedules'][str(group)]