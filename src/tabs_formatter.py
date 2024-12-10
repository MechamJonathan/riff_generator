import os
import datetime


def format_tabs(riff):
    tabs = [f"{string}|" for string in riff.fretboard.tuning]

    for bar in riff.get_riff():
        for beat in bar:
            if isinstance(beat, list):
                for i, (string_index, fret) in enumerate(beat):
                    if len(str(fret)) == 2:
                        tabs[string_index] += f"{fret}-"
                    else:
                        tabs[string_index] += f"{fret}--"

                for i in range(len(tabs)):
                    if i not in [note[0] for note in beat]:
                        tabs[i] += "---"
            
            elif beat is None:
                for i in range(len(tabs)):
                    tabs[i] += "---"

            elif beat == 0:
                tabs[0] += "0--"
                for i in range(1, len(tabs)):
                    tabs[i] += "---"
        for i in range(len(tabs)):
            tabs[i] += "|"

    return tabs[::-1]

def save_riff_to_file(riff, filename="riff.txt"):
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    my_riffs_dir = os.path.join(root_dir, "MyRiffs")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    if not os.path.exists(my_riffs_dir):
        os.makedirs(my_riffs_dir)
    
    filepath = os.path.join(my_riffs_dir, f"{filename}-{timestamp}")

    try:
        with open(filepath, "w") as file:
            for line in riff:
                file.write(line + "\n")
        print(f"Riff saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving the riff: {e}")

