import unittest
import re
from scale import Scale
from fretboard import Fretboard
from riff import Riff
from tabs_formatter import format_tabs

class TestTabFormatting(unittest.TestCase):
    def test_tab_format(self):
        tuning = "Standard_E"
        chosen_scale = Scale(key="E", scale_type="Minor")
        fretboard = Fretboard(tuning)
        riff = Riff(chosen_scale, fretboard)

        generated_tabs = format_tabs(riff)

        self.assertEqual(len(generated_tabs), len(riff.fretboard.tuning))

        line_lengths = [len(line) for line in generated_tabs]
        self.assertTrue(all(length == line_lengths[0] for length in line_lengths))

if __name__ == "__main__":
    unittest.main()
