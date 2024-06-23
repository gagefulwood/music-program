import tkinter as tk
from tkinter import ttk
import pygame.midi

class PianoRoll:
    def __init__(self, parent_notebook: ttk.Notebook):
        self.create_piano_roll_frame(parent_notebook)
        self.create_piano_roll_canvas()
        self.create_key_dict()
        self.initialize_midi()
        self.piano_roll_canvas.bind("<Configure>", self.on_resize)

    def create_piano_roll_frame(self, parent_notebook: ttk.Notebook):
        self.piano_roll_frame = tk.Frame(parent_notebook)
        parent_notebook.add(self.piano_roll_frame, text="Piano")

    def create_piano_roll_canvas(self):
        self.piano_roll_canvas = tk.Canvas(self.piano_roll_frame, bg="white")
        self.piano_roll_canvas.pack(fill=tk.BOTH, expand=True)

    def create_key_dict(self):
        self.key_dict = {"C": None, "C#/Db": None, "D": None,
                         "D#/Eb": None, "E": None, "F": None,
                         "F#/Gb": None, "G": None, "G#/Ab": None,
                         "A": None, "A#/Bb": None, "B": None}

    def initialize_midi(self):
        pygame.midi.init()
        self.midi_out = pygame.midi.Output(pygame.midi.get_default_output_id())

    def play_note(self, note):
        velocity = 127
        self.midi_out.note_on(note, velocity)
        self.piano_roll_canvas.after(500, lambda: self.midi_out.note_off(note, velocity))

    def draw_white_keys(self):
      self.piano_roll_canvas.delete("all")
      width = self.piano_roll_canvas.winfo_width() // 14
      height = self.piano_roll_canvas.winfo_height()
      x1 = 0

      # Mapping white keys to their positions and pitches
      key_positions = {
        "C": (x1, 60), "D": (x1 + width, 62), "E": (x1 + width * 2, 64),
        "F": (x1 + width * 3, 65), "G": (x1 + width * 4, 67), "A": (x1 + width * 5, 69),
        "B": (x1 + width * 6, 71), "C2": (x1 + width * 7, 72), "D2": (x1 + width * 8, 74),
        "E2": (x1 + width * 9, 76), "F2": (x1 + width * 10, 77), "G2": (x1 + width * 11, 79),
        "A2": (x1 + width * 12, 81), "B2": (x1 + width * 13, 83)
      }

      for key, (x_pos, pitch) in key_positions.items():
         white_button = tk.Button(self.piano_roll_canvas, text=key, fg="black", bg="white", anchor='s', relief="raised", command=lambda pitch=pitch: self.play_note(pitch))
         white_button.place(x=x_pos, y=0, width=width, height=height)
         self.key_dict[key] = white_button

    def draw_black_keys(self):
         width = self.piano_roll_canvas.winfo_width() // 28
         height = self.piano_roll_canvas.winfo_height() // 2
         x1 = width * 3 // 2  # Position the first black key

         # Mapping black keys to their positions and pitches
         key_positions = {
        "C#/Db": (x1, 61), "D#/Eb": (x1 + width * 2, 63), "F#/Gb": (x1 + width * 6, 66),
        "G#/Ab": (x1 + width * 8, 68), "A#/Bb": (x1 + width * 10, 70), "C#/Db2": (x1 + width * 14, 73),
        "D#/Eb2": (x1 + width * 16, 75), "F#/Gb2": (x1 + width * 20, 78), "G#/Ab2": (x1 + width * 22, 80),
        "A#/Bb2": (x1 + width * 24, 82)
         }

         for key, (x_pos, pitch) in key_positions.items():
            black_button = tk.Button(self.piano_roll_canvas, text=key, fg="white", bg="black", anchor='s', relief="raised", command=lambda pitch=pitch: self.play_note(pitch))
            black_button.place(x=x_pos, y=0, width=width, height=height)
            self.key_dict[key] = black_button

    def draw_piano_roll(self):
        self.draw_white_keys()
        self.draw_black_keys()

    def on_resize(self, event):
        self.draw_piano_roll()

