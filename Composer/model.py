class ChordModel:
    def __init__(self):
        self.notes = [
            "C","C#","D","D#",
            "E","F","F#","G",
            "G#","A","A#","B"
        ]
        self.qualities = {
            "major": [0,4,7],
            "minor": [0,3,7],
            "diminished": [0,3,6],
            "augmented": [0,4,8],
            "major7": [0,4,7,11],
            "minor7": [0,3,7,10]
        }

    def get_chord_notes(self, root, quality):
        intervals = self.get_intervals(quality)
        root_index = self.notes.index(root)
        chord_notes = []
        for interval in intervals:
            note_index = (root_index + interval) % 12
            chord_notes.append(self.notes[note_index])
        return chord_notes

    def get_intervals(self, quality):
        return self.qualities[quality]