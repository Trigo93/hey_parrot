def load_prompt(file_path, text):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().format(user_input=text)