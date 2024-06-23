import threading
import time
import customtkinter as ctk
from tkinter import ttk
import json
import webbrowser
import os

# from workspace.verbindung import set_link_coverEbook

# note to Konrad: in the main function start_second_ui(prompt) i give prompt directly through parameter "prompt". you
# dont need to import anything or write a extra func to save the prompt.



ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

geometry = "640x400"

# Globale Variablen
final_title = None
wait_for_title = False
wait_for_chapter = True

def submit_prompt():
    global ui_prompt  # Use global to modify the global variables
    ui_genre = genre_combobox.get()  # Get the selected genre from the combobox
    ui_thema = thema_entry.get()  # Get the selected gattung from the combobox
    ui_tonali = tonali_combobox.get()
    ui_kapitel = kapitel_combobox.get()
    ui_prompt = {
        "genre": ui_genre,
        "thema": ui_thema,
        "tonalitaet": ui_tonali,
        "anzahlvonkapitel": ui_kapitel
    }
    ui_prompt = json.dumps(ui_prompt, ensure_ascii=False, indent=2)
    root.quit()  # Stop the mainloop
    root.destroy()


def copy_to_clipboard(label):
    try:
        label.configure(state="normal")
        text = label.get("1.0", "end-1c")
        label.configure(state="disabled")
        # Die Zwischenablage löschen und den neuen Text einfügen
        second_root.clipboard_clear()
        second_root.clipboard_append(text)
    except Exception as e:
        print("Fehler", "Ein Fehler ist aufgetreten: " + str(e))


def open_url(url):
    webbrowser.open(url)


def select_title(title_json):
    set_wait_for_title(True)
    # title_dict = json.loads(title_json,strict=False)
    title_dict = title_json
    print(title_dict)
    wait_label.configure(text="Wählen Sie einen der folgenden Titel und Idee für Ihr Ebook:")
    global titel_textbox, titel_combobox, titel_button
    titel_text = str()
    titel_nums = list()
    for idea in title_dict:
        titel_nums.append(idea)
        idea_text = f'{idea}:\n {title_dict[idea]["Titel"]}\n {title_dict[idea]["Idea"]}\n'
        titel_text = titel_text + idea_text
        print(titel_text)
    titel_textbox = ctk.CTkTextbox(wait_root, wrap="word", width=800)
    titel_textbox.pack()
    titel_textbox.insert(ctk.END, titel_text)
    titel_textbox.configure(state="disabled")
    titel_combobox = ctk.CTkComboBox(wait_root, values=titel_nums)
    titel_combobox.pack()
    titel_button = ctk.CTkButton(wait_root, text="Weiter",
                                 command=lambda: delete_title_elements(title_dict[titel_combobox.get()]))
    titel_button.pack()


def delete_title_elements(final_title):
    wait_label.configure(text="Warte, während das E-Book generiert wird.")
    titel_textbox.destroy()
    titel_combobox.destroy()
    titel_button.destroy()
    final_title_string = f'Titel: {final_title["Titel"]}\nIdea: {final_title["Idea"]}'
    set_final_title(final_title_string)
    set_wait_for_title(False)


def select_chapter(chapter_json):
    global chapter_dict
    chapter_dict = json.loads(chapter_json)
    chapter_label.configure(text="Kapitel bearbeiten (optional)")
    chapter_num_label = ctk.CTkLabel(chapter_root, text="")
    chapter_num_label.pack()
    chapter_titel_textbox = ctk.CTkTextbox(chapter_root, wrap="word", width=800, height=10)
    chapter_titel_textbox.pack()
    chapter_inhalt_textbox = ctk.CTkTextbox(chapter_root, wrap="word", width=800, height=200)
    chapter_inhalt_textbox.pack()
    chapter_button = ctk.CTkButton(chapter_root, text="Weiter",
                                   command=lambda: update_chapters(chapter_titel_textbox.get("1.0", ctk.END),
                                                                   chapter_inhalt_textbox.get("1.0", ctk.END),
                                                                   chapter))
    chapter_button.pack()
    chapter_num = 1
    for chapter in chapter_dict:
        set_button_not_pressed(True)
        chapter_num_label.configure(text=f"Kapitel {chapter_num}")
        chapter_num += 1
        chapter_titel_textbox.delete("1.0", ctk.END)
        chapter_inhalt_textbox.delete("1.0", ctk.END)
        chapter_titel_textbox.insert(ctk.END, chapter_dict[chapter]["Kapitel Titel"])
        chapter_inhalt_textbox.insert(ctk.END, chapter_dict[chapter]["Kapitel Inhalt"])

        while get_button_not_pressed():
            time.sleep(1)
    set_final_chapters(chapter_dict)
    set_wait_for_chapter(False)
    chapter_button.destroy()
    chapter_inhalt_textbox.destroy()
    chapter_titel_textbox.destroy()
    chapter_num_label.destroy()
    chapter_label.configure(text="Kapitel Bearbeiten Abgeschlossen.")
    chapter_final_button = ctk.CTkButton(chapter_root, text="Weiter", command=chapter_root.destroy)
    chapter_final_button.pack()


def set_button_not_pressed(status: bool):
    global button_not_pressed
    button_not_pressed = status


def get_button_not_pressed():
    return button_not_pressed


def update_chapters(titel_text, chapter_text, chapter):
    chapter_dict[chapter]["Kapitel Titel"] = titel_text.strip()
    chapter_dict[chapter]["Kapitel Inhalt"] = chapter_text.strip()
    set_button_not_pressed(False)


def set_final_title(new_final_title):
    global final_title
    final_title = new_final_title


def get_final_title():
    return final_title


def set_wait_for_title(status: bool):
    global wait_for_title
    wait_for_title = status


def get_wait_for_title():
    return wait_for_title


def set_wait_for_chapter(status: bool):
    global wait_for_chapter
    wait_for_chapter = status


def get_wait_for_chapter():
    return wait_for_chapter


def set_final_chapters(new_final_chapters):
    global final_chapters
    final_chapters = json.dumps(new_final_chapters)


def get_final_chapters():
    return final_chapters


def html_generated():
    wait_label.configure(text="Das E-Book ist fast fertig, klicken Sie auf \"Weiter\" um fortzufahren.")
    continue_button = ctk.CTkButton(wait_root, text="Weiter", command=wait_root.destroy)
    continue_button.pack()


def change_thema_entry(thema):
    thema_entry.delete(0, ctk.END)
    thema_entry.insert(0, thema)


def start_ui():  # fur User Input am Anfang
    global root, genre_combobox, tonali_combobox, kapitel_combobox, thema_entry
    root = ctk.CTk()
    root.title("E-Book Generator")
    root.geometry(geometry)

    # Genre selection
    genre_label = ctk.CTkLabel(root, text="Entscheide dich für ein Genre:")
    genre_label.grid(row=0, column=0)

    genres = ["Fantasy", "Thriller", "Horror", "Liebesroman", "Historischer Roman", "Krimi", "Utopie", "Western",
              "Kinderbuch", "Science Fiction", "Steampunk", "Gesellschaftsroman"]
    genre_combobox = ctk.CTkComboBox(root, values=genres)
    genre_combobox.grid(row=0, column=1)

    # Thema selection
    thema_label = ctk.CTkLabel(root, text="Gib das ein Thema an:")
    thema_label.grid(row=1, column=0)

    themen = ["Studentenleben", "Zauberland", "Piraten", "Parallelwelt", "Viktorianisches England", "Unbewohnte Insel",
              "Welt von Game of Thrones", "Altes Ägypten", "Stadt der Zukunft", "Archäologische Expedition",
              "Moderne Großstadt", "Psychatrische Klinik", "Postapokalyptische Wüste", "Raumschiff",
              "Everest Besteigung"]
    thema_combobox = ctk.CTkComboBox(root, values=themen, command=change_thema_entry)
    thema_combobox.grid(row=1, column=1)
    thema_entry = ctk.CTkEntry(root, width=310)
    thema_entry.grid(row=2, column=0, columnspan=2)

    # Tonalität selection
    tonali_label = ctk.CTkLabel(root, text="Lege die Tonalität fest:")
    tonali_label.grid(row=3, column=0)

    tonalis = ["neutral", "satirisch", "humorvoll", "kindisch", "gruselig", "melancholisch", "mystisch", "spannend",
               "romantisch"]
    tonali_combobox = ctk.CTkComboBox(root, values=tonalis)
    tonali_combobox.grid(row=3, column=1)

    # Anzahl Kapitel selection
    kapitel_label = ctk.CTkLabel(root, text="Anzahl der Kapitel:")
    kapitel_label.grid(row=4, column=0)

    kapitel = ["2","3", "4", "5", "6", "7", "8", "9"]
    kapitel_combobox = ctk.CTkComboBox(root, values=kapitel)
    kapitel_combobox.grid(row=4, column=1)

    # Generate button
    generate_button = ctk.CTkButton(root, text="E-Book generieren", command=submit_prompt)
    generate_button.grid(row=5, column=1)

    root.mainloop()
    return ui_prompt  # Return the selections after the UI has closed


def start_second_ui(prompt):  # für book cover
    global second_root, cover_link_entry, saved_link
    second_root = ctk.CTk()
    second_root.title("E-Book Generator")
    second_root.geometry(geometry)

    saved_link = None  # Initialize saved_link variable

    def save_embed_link():
        global saved_link
        saved_link = cover_link_entry.get()  # Get the value of cover_link_entry
        second_root.destroy()  # Close the UI

    heading = ctk.CTkFrame(second_root, width=400)
    heading.pack(anchor="w")
    heading_label = ctk.CTkLabel(heading, text="Nutze diesen Prompt um ein Cover für das E-Book zu erstellen.")
    heading_label.pack(anchor="w")
    cover = ctk.CTkFrame(second_root, width=400)
    cover.pack(anchor="w")
    cover_link = ctk.CTkFrame(second_root, width=400)
    cover_link.pack()
    cover_link_label = ctk.CTkLabel(cover_link,
                                    text="Kopiere jetzt den Embed-Code HTML (Vollansicht-Link) und füge ihn hier ein:")
    cover_link_label.grid(row=0, column=0)
    cover_link_entry = ctk.CTkEntry(cover_link, width=500)
    cover_link_entry.grid(row=1, column=0, sticky="w")
    cover_link_button = ctk.CTkButton(cover_link, text="Link speichern", command=save_embed_link)
    cover_link_button.grid(row=1, column=1)

    # Text mit dem Cover Prompt
    cover_prompt_label = ctk.CTkTextbox(cover, wrap="word", height=160, width=500)
    cover_prompt_label.grid(row=0, column=0, sticky="w")
    cover_prompt_label.insert(ctk.END, prompt)
    cover_prompt_label.configure(state="disabled")

    # Button zum Kopieren des Texts
    copy_button = ctk.CTkButton(cover, text="Kopieren", command=lambda: copy_to_clipboard(cover_prompt_label))
    copy_button.grid(row=0, column=1, sticky="se")

    # Weiterleitung zu Bing Copilot
    copilot_label = ctk.CTkLabel(cover, text="Wir empfehlen dafür den Bing Copilot zu verwenden.")
    copilot_label.grid(row=1, column=0)
    copilot_button = ctk.CTkButton(cover, text="Zu Copilot",
                                   command=lambda: open_url("https://www.bing.com/images/create"))
    copilot_button.grid(row=1, column=1)

    # Weiterleitung zu Imgbb
    """
    imgbb_label = ctk.CTkLabel(cover, text="Lade das online hoch, wir empfehlen imgbb")
    imgbb_label.grid(row=2, column=0)
    imgbb_button = ctk.CTkButton(cover, text="Zu imgbb", command=lambda: open_url("https://de.imgbb.com/"))
    imgbb_button.grid(row=2, column=1)
    """

    second_root.mainloop()

    return saved_link


def start_wait_ui():
    global wait_root, wait_label
    wait_root = ctk.CTk()  # Verwendet Customtkinter für das zweite Fenster
    wait_root.title("E-Book Generator")
    wait_root.geometry(geometry)

    wait_label = ctk.CTkLabel(wait_root, text="Warte, während das E-Book generiert wird.")
    wait_label.pack()

    wait_root.mainloop()


def start_chapter_ui():
    global chapter_root, chapter_label
    chapter_root = ctk.CTk()
    chapter_root.title("E-Book Generator")
    chapter_root.geometry(geometry)

    chapter_label = ctk.CTkLabel(chapter_root, text="Kapitel werden geladen...")
    chapter_label.pack()
    set_wait_for_chapter(True)

    if not get_wait_for_chapter():
            chapter_root.quit()
            chapter_root.destroy()

    chapter_root.mainloop()


class MyThread(threading.Thread):
    def __init__(self, iD):
        threading.Thread.__init__(self)
        self.iD = iD

    def run(self):
        print("Starte Thread", self.iD)
        if self.iD == 1:
            start_wait_ui()
        if self.iD == 2:
            start_chapter_ui()
        print("Beende Thread", self.iD)

    def set_iD(self, new_iD):
        self.iD = new_iD


# This allows the module to be imported without immediately running the UI
if __name__ == "__main__":
    # start_ui()
    start_second_ui()
    # link = start_second_ui("Prompt text")
    # print("Link entered:", link)
    # start_wait_ui(stop_event=None)
