
from scale import Scale
from fretboard import Fretboard
from riff import Riff
from tabs_formatter import format_tabs


def main():

    print("\nWelcome to the Simple Guitar Riff Generator!\n")
    print("""\n██████──██
─██████████─────▄─▄─▄
──███O▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
───████████─────▀─▀─▀
────██──██\n""")

    key = input("Choose one of the available keys (E): ") or "E"
    scale_type = input("Choose a scale (Major, Minor, Pentatonic): ") or "Pentatonic"
    tuning = input("Choose tuning (Standard_E, Drop_D): \n") or "Standard_E"

    chosen_scale = Scale(key, scale_type)
    fretboard = Fretboard(tuning)
    riff = Riff(chosen_scale, fretboard)

    #print(riff.get_riff())
    print("\n".join(format_tabs(riff)))


if __name__ == '__main__':
    main()

