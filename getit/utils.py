import json


def load_data(file_path):
    with open(file_path) as file:
        return json.load(file)


def load_template(file_path):
    with open(file_path) as file:
        return file.read()
