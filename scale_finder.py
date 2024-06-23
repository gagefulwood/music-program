import tkinter as tk
from tkinter import ttk

class ScaleFinder():
    def __init__(self, parent_notebook: ttk.Notebook):
        self.create_scale_finder_frame(parent_notebook)
        self.create_chords_frame()
        self.create_settings_frame()
    
    def create_scale_finder_frame(self, parent_notebook: ttk.Notebook):
        self.scale_finder_frame = ttk.Frame(parent_notebook)
        parent_notebook.add(self.scale_finder_frame, text="Scale Finder")

    def create_chords_frame(self):
        self.chords_frame = tk.Frame(self.scale_finder_frame, bg="purple", bd=1)
        self.chords_frame.pack(side="left", padx=10, pady=10, fill="both", expand=True)

    def create_settings_frame(self):
        self.settings_frame = tk.Frame(self.scale_finder_frame, bg="red", bd=1)
        self.settings_frame.pack(side="right", padx=10, pady=10, fill="both", expand=True)
