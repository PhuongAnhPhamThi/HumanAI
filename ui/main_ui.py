import tkinter as tk
from tkinter import ttk
import json
import webbrowser
from workspace.verbindung import set_link_coverEbook


def some_function():
    from workspace.verbindung import prompt_coverEbook
    global cover_prompt
    cover_prompt = prompt_coverEbook


def submit_prompt():
    global ui_prompt  # Use global to modify the global variables
    ui_genre = genre_combobox.get()  # Get the selected genre from the combobox
    ui_gattung = gattung_combobox.get()  # Get the selected gattung from the combobox
    ui_prompt = {
        "genre": ui_genre,
        "gattung": ui_gattung
    }
    ui_prompt = json.dumps(ui_prompt, ensure_ascii=False, indent=2)
    root.quit()  # Stop the mainloop
    root.destroy()


def copy_to_clipboard(label):
    try:
        label.config(state="normal")
        text = label.get("1.0", "end-1c")
        label.config(state="disabled")
        # Die Zwischenablage löschen und den neuen Text einfügen
        second_root.clipboard_clear()
        second_root.clipboard_append(text)
    except Exception as e:
        print("Fehler", "Ein Fehler ist aufgetreten: " + str(e))


def open_url(url):
    webbrowser.open(url)


def save_embed_link():
    set_link_coverEbook(cover_link_entry.get())


def start_ui():
    global root, genre_combobox, gattung_combobox
    root = tk.Tk()
    root.title("E-Book Generator")

    # Genre selection
    genre_label = tk.Label(root, text="Entscheide dich für ein Genre:")
    genre_label.grid(row=0, column=0)

    genres = ["Komödie", "Fantasy", "Thriller", "Horror", "Liebesroman", "Krimi", "Science Fiction", "Steampunk",
              "Gesellschaftsroman"]
    genre_combobox = ttk.Combobox(root, values=genres)
    genre_combobox.grid(row=0, column=1)

    # Gattung selection
    gattung_label = tk.Label(root, text="Wähle eine Gattung:")
    gattung_label.grid(row=1, column=0)

    gattungen = ["Prosatext", "Gedicht", "Theaterstück"]
    gattung_combobox = ttk.Combobox(root, values=gattungen)
    gattung_combobox.grid(row=1, column=1)

    # Generate button
    generate_button = tk.Button(root, text="E-Book generieren", command=submit_prompt)
    generate_button.grid(row=2, column=1)

    root.mainloop()
    return ui_prompt  # Return the selections after the UI has closed


def start_second_ui():
    global second_root, cover_link_entry
    second_root = tk.Tk()
    second_root.title("E-Book Generator")

    heading = tk.Frame(second_root, width=400)
    heading.pack()
    heading_label = tk.Label(heading, text="Nutze diesen Prompt um ein Cover für das E-Book zu erstellen.")
    heading_label.pack()
    cover = tk.Frame(second_root, width=400)
    cover.pack(anchor="w")
    cover_link = tk.Frame(second_root, width=400)
    cover_link.pack()
    cover_link_label = tk.Label(cover_link, text="Kopiere jetzt den Embed-Code HTML (Vollansicht-Link) und füge ihn hier ein:")
    cover_link_label.grid(row=0, column=0)
    cover_link_entry = tk.Entry(cover_link, width=67)
    cover_link_entry.grid(row=1, column=0, sticky="w")
    cover_link_button = tk.Button(cover_link, text="Link speichern", command=lambda: save_embed_link())
    cover_link_button.grid(row=1, column=1)

    # Text mit dem Cover Prompt
    cover_prompt_label = tk.Text(cover, wrap="word", height=8, width=50)
    cover_prompt_label.grid(row=0, column=0, sticky="w")
    some_function()
    cover_prompt_label.insert(tk.END, cover_prompt)
    cover_prompt_label.config(state="disabled")

    # Button zum Kopieren des Texts
    copy_button = tk.Button(cover, text="Kopieren", command=lambda: copy_to_clipboard(cover_prompt_label))
    copy_button.grid(row=0, column=1, sticky="se")

    # Weiterleitung zu Bing Copilot
    copilot_label = tk.Label(cover, text="Wir empfehlen dafür den Bing Copilot zu verwenden.")
    copilot_label.grid(row=1, column=0)
    copilot_button = tk.Button(cover, text="Zu Copilot", command=lambda: open_url("https://www.bing.com/images/create"))
    copilot_button.grid(row=1, column=1)

    # Weiterleitung zu Imgbb
    imgbb_label = tk.Label(cover, text="Lade das online hoch, wir empfehlen imgbb")
    imgbb_label.grid(row=2, column=0)
    imgbb_button = tk.Button(cover, text="Zu imgbb", command=lambda: open_url("https://de.imgbb.com/"))
    imgbb_button.grid(row=2, column=1)

    second_root.mainloop()


# This allows the module to be imported without immediately running the UI
if __name__ == "__main__":
    start_ui()
    start_second_ui()
