from model import ChordModel
from view import ChordView

class ChordController:
    def __init__(self):
        self.model = ChordModel()
        self.view = ChordView(self)
        self.view.mainloop()

    def find_chord(self):
        root = self.view.get_chord_name().upper()
        chord_type = self.view.get_chord_quality()
        notes = self.model.get_chord_notes(root, chord_type)
        if notes:
            self.view.display_chord_notes(notes)
        else:
            self.view.display_error("Chord not found or invalid input")

    def get_notes(self):
        return self.model.notes

    def get_chord_qualities(self):
        return self.model.qualities
    
    def get_first_chord_quality(self):
        return next(iter(self.model.qualities))

if __name__ == "__main__":
    ChordController()
