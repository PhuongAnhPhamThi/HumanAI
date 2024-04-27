import tkinter as tk


def submit_prompt():
    global ui_prompt  # Use the global keyword to modify the global variable
    ui_prompt = prompt_entry.get()  # Get input from the entry widget
    root.quit()  # Use quit() to stop the mainloop, not destroy()


def start_ui():
    global root, prompt_entry
    root = tk.Tk()
    root.title("E-Book Generator")

    prompt_label = tk.Label(root, text="Worum soll es in dem Buch gehen?")
    prompt_label.pack()

    prompt_entry = tk.Entry(root, width=50)
    prompt_entry.pack()

    generate_button = tk.Button(root, text="E-Book generieren", command=submit_prompt)
    generate_button.pack()

    root.mainloop()
    return ui_prompt  # Return the prompt after the UI has closed


# This allows the module to be imported without immediately running the UI
if __name__ == "__main__":
    start_ui()
