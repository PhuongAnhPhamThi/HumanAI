import tkinter as tk
from tkinter import ttk
import json


def submit_prompt():
    global ui_prompt  # Use global to modify the global variables
    ui_genre = genre_combobox.get()  # Get the selected genre from the combobox
    ui_gattung = gattung_combobox.get()  # Get the selected gattung from the combobox
    ui_prompt = {
        "genre": ui_genre,
        "gattung": ui_gattung
    }
    ui_prompt = json.dumps(ui_prompt, ensure_ascii=False, indent=2)
    ui_prompt = '"""' + ui_prompt + '"""'
    root.quit()  # Stop the mainloop


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


# This allows the module to be imported without immediately running the UI
if __name__ == "__main__":
    start_ui()
