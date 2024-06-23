import tkinter as tk
from tkinter import ttk
from chord_finder import ChordFinder
from scale_finder import ScaleFinder
from piano_roll import PianoRoll

class GUI():
    def __init__(self):
        self.create_window()
        self.create_primary_frame()
        self.create_feature_notebook()
        self.create_midi_notebook()
        
        self.run()

    def create_window(self): # Parent window to the primary frame (Application Window)
        self.window = tk.Tk()
        self.window.title("Music App")
        self.window_width = 800
        self.window_height = 400
        self.window.geometry(f"{self.window_width}x{self.window_height}")

    def create_primary_frame(self): # Parent frame to Feature frame & Midi frame (Primary frame)
        self.primary_frame = tk.Frame(self.window, bg="lightblue", bd=1)
        self.primary_frame.pack(padx=10, pady=10, fill="both", expand=True)

    def create_feature_notebook(self):
        self.feature_notebook = ttk.Notebook(self.primary_frame)
        self.feature_notebook.pack(fill=tk.BOTH, expand=True)
        # create chord finder tab
        self.chord_finder_tab = ChordFinder(self.feature_notebook)
        # create scale finder tab
        self.scale_finder_tab = ScaleFinder(self.feature_notebook)
        # create chord progression maker tab

    def create_midi_notebook(self): # Parent frame to Piano Roll & Fretboard frame (Lower Frame)
        self.midi_notebook = ttk.Notebook(self.primary_frame)
        self.midi_notebook.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        # create piano roll tab
        self.piano_roll_tab = PianoRoll(self.midi_notebook)
        # create guitar fretboard tab (to-do way later using caged for chords)

    def run(self):
        self.window.mainloop()

test = GUI()