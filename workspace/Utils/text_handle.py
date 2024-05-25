import os

file_path = os.path.join("workspace") + "/"


def write_to_txt_file(txt: str, actiontype: str, rolle: str, action: str, text: str):
    with open(file_path + txt, actiontype, encoding="utf-8") as file:
        file.write("******" + rolle + " - " + action + " :\n")
        file.write(
            text + " \n\n" + "-------------------------------------------------------------------------------------------------" + "\n\n\n")


def write_to_txt_file_simple(txt: str, actiontype: str, text: str):
    with open(file_path + txt, actiontype, encoding="utf-8") as file:
        file.write(text)


def read_from_txt_file(txt: str, actiontype: str):
    with open(file_path + txt, actiontype, encoding="utf-8") as file:
        str_to_load = file.read()
    return str_to_load
