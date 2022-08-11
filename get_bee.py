import json


def get_bee(*args):
    with open("bee.json", "r") as file:
        return json.load(file)
