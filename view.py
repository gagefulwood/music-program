import tkinter as tk

class ChordView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Chord Finder")
        self.geometry("250x200")
        self.minsize(250,200)
        self.create_widgets()


    def create_label(self, text):
        label = tk.Label(self, text=text)
        label.pack(pady=5)
        return label

    def create_option_menu(self, variable, *values):
        menu = tk.OptionMenu(self, variable, *values)
        menu.pack(pady=5)
        return menu
    
    def create_button(self, text, command):
        button = tk.Button(self, text=text, command=command)
        button.pack(pady=5)
        return button

    def create_widgets(self):
        self.root_label = self.create_label("Root Note:")
        self.root_note = tk.StringVar(self)
        self.root_note.set(self.controller.get_notes()[0])
        self.root_menu = self.create_option_menu(self.root_note,
                                                 *self.controller.get_notes())

        self.quality_label = self.create_label("Quality:")
        self.chord_quality = tk.StringVar(self)
        self.chord_quality.set(self.controller.get_first_chord_quality())
        self.quality_menu = self.create_option_menu(self.chord_quality,
                                                    *self.controller.get_chord_qualities())
        
        self.find_button = self.create_button("Find Chord",self.controller.find_chord)
        self.chord_label = self.create_label("")

    def get_chord_name(self):
        return self.root_note.get()

    def get_chord_quality(self):
        return self.chord_quality.get()

    def display_chord_notes(self, notes):
        notes_str = ", ".join(notes)
        self.chord_label.config(text=f"Notes: {notes_str}")

    def display_error(self, message):
        self.chord_label.config(text=message)