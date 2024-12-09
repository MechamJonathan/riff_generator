import unittest
from scale import Scale


class TestScales(unittest.TestCase):
    def test_scale_notes(self):
        e_minor_scale = Scale("E", "Minor")
        e_major_scale = Scale("E", "Major")
        self.assertEqual(e_minor_scale.get_scale_notes(), ["E", "F#", "G", "A", "B", "C", "D"] )
        self.assertEqual(e_major_scale.get_scale_notes(), ["E", "F♯", "G♯", "A", "B", "C♯", "D♯"])


if __name__ == "__main__":
    unittest.main()
