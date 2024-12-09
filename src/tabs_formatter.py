
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