
from scale import Scale
from fretboard import Fretboard
from riff import Riff
from tabs_formatter import format_tabs, save_riff_to_file


def main():

    print("\nWELCOME TO SIMPLE METAL RIFF GENERATOR!\n")
    print("""██████──██
─██████████─────▄─▄─▄
──███O▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
───████████─────▀─▀─▀
────██──██\n""")
    
    key, scale_type, tuning = user_input()

    chosen_scale = Scale(key, scale_type)
    fretboard = Fretboard(tuning)
    riff = Riff(chosen_scale, fretboard)

    print("\nYOUR RIFF HAS BEEN GENERATED")
    print(f"Key: {key}\nScale: {scale_type}\nTuning: {tuning}\n")
    print("\n".join(format_tabs(riff)) + "\n")

    save_riff_dialog(riff)


def user_input():
    acceptable_keys = ["E"]
    acceptable_scale_types = ["Major", "Minor", "Pentatonic"]
    acceptable_tunings = ["Standard_E", "Drop_D"]
    
    while True:
        try:
            key = input("Choose one of the available keys (E): ") or "E"
            if key in acceptable_keys:
                break
            else:
                print("Please choose from one of the keys listed")
        except ValueError:
            print("Invalid input. Please enter a key.")
    
    while True:
        try:
            scale_type = input("Choose a scale (Major, Minor, Pentatonic): ") or "Pentatonic"
            if scale_type in acceptable_scale_types:
                break
            else:
                print("Please choose from one of the scales listed")
        except ValueError:
            print("Invalid input. Please enter a scale.")
    
    while True:
        try:
            tuning = input("Choose tuning (Standard_E, Drop_D):") or "Standard_E"
            if tuning in acceptable_tunings:
                break
            else:
                print("Please choose from one of the tunings listed")
        except ValueError:
            print("Invalid input. Please enter a tuning from the list.")

    return key, scale_type, tuning

def save_riff_dialog(riff):
    while True:
        try:
            key = input("Would you like to save your riff? (Y/N): ") or "N"
            if key == "N":
                break
            else:
                save_riff_to_file(format_tabs(riff))
                break
        except ValueError:
            print("Invalid input. Please enter Y or N.")

if __name__ == '__main__':
    main()