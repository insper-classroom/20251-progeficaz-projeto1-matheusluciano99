import json


def load_data(data):
    file_path = f"static/data/{data}"
    with open(file_path) as file:
        return json.load(file)


def load_template(template_name):
    file_path = f"static/templates/{template_name}"
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
