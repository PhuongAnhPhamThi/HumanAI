import os

file_path = os.path.join("workspace") + "/"


def write_to_txt_file(txt: str, actiontype: str, rolle: str, action: str, text: str):
    with open(file_path + txt, actiontype, encoding="utf-8") as file:
        file.write("******" + rolle + " - " + action + " :\n")
        file.write(
            text + " \n\n" + "-------------------------------------------------------------------------------------------------" + "\n\n\n")
