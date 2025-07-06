import json

def load_prompt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
    
def load_shots(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)