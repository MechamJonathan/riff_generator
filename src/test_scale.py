import unittest
from scale import Scale

class TestScales(unittest.TestCase):
    def test_scale_notes(self):
        e_minor_scale = Scale("E", "Minor")
        e_major_scale = Scale("E", "Major")
        e_pentatonic_scale = Scale("E", "Pentatonic")
        self.assertEqual(e_minor_scale.get_scale_notes(), ["E", "F#", "G", "A", "B", "C", "D"] )
        self.assertEqual(e_major_scale.get_scale_notes(), ["E", "F#", "G#", "A", "B", "C#", "D#"])
        self.assertEqual(e_pentatonic_scale.get_scale_notes(), ["E", "G", "A", "B", "D"])

if __name__ == "__main__":
    unittest.main()
