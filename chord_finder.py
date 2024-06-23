import tkinter as tk
from tkinter import ttk

class ChordFinder():
    def __init__(self, parent_notebook: ttk.Notebook):
        self.create_chord_finder_frame(parent_notebook)
        self.create_key_dict()
        self.create_chords_frame()
        self.create_settings_frame()
    
    def create_chord_finder_frame(self, parent_notebook: ttk.Notebook):
        self.chord_finder_frame = ttk.Frame(parent_notebook)
        parent_notebook.add(self.chord_finder_frame, text="Chord Finder")
    
    def create_key_dict(self):
        self.key_dict = {"C": None, "C#/Db": None, "D": None,
                         "D#/Eb": None, "E": None, "F": None,
                         "F#/Gb": None, "G": None, "G#/Ab": None,
                         "A": None, "A#/Bb": None, "B": None}
        
    def create_chords_frame(self):
        self.chords_frame = tk.Frame(self.chord_finder_frame, bg="lightgreen", bd=1)
        self.chords_frame.pack(side="left", padx=10, pady=10, fill="both", expand=True)

        #for key in self.key_dict:
            #toggle_button = tk.Button(self.chords_frame, text=key, width=10, bg='red', command=toggle)
            #toggle_button.pack(pady=20)
            

    def create_settings_frame(self):
        self.settings_frame = tk.Frame(self.chord_finder_frame, bg="orange", bd=1)
        self.settings_frame.pack(side="right", padx=10, pady=10, fill="both", expand=True)

    