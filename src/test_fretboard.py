import unittest
from fretboard import Fretboard


class TestFretboard(unittest.TestCase):
    def test_fretboard_strings(self):
        fretboard = Fretboard("Standard_E")
        self.assertEqual(fretboard.get_strings(), [["E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#"],
                              ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"],
                              ["D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#"]])

if __name__ == "__main__":
    unittest.main()
