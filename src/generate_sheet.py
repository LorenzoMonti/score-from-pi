import os
import sys
import Utils


if __name__ == '__main__':
    
    """ 
    Lilypond syntax:
        - diesis: is
        - flat: es
    """
    
    if len(sys.argv) != 2:
        print('USAGE: generate_sheet.py filename')
        sys.exit(1)

    filename = "../res/lilypond/" + sys.argv[1] + ".ly"
    pi_file = "../res/pi/pi_10000.txt"
    digit_mapping = Utils.read_key_file("../config/key.json")
    notes = list()
    
    # open pi file
    with open(pi_file, "r") as f:
        contents = f.readline()

    # digit-notes mapping
    for char in contents:
        if not char == ".":
            notes.append(digit_mapping[char] + " ")

    # write notes file
    with open(filename, "a") as f:
        f.write('\\version "2.22.1" \n \score{\n {\n  \key des \major \n')
        f.writelines(notes)
        f.write('}\n  \layout{ }\n  \midi { \\tempo 4=100 }\n}')

    os.system("lilypond " + filename) # on bash
    os.system("mv *.pdf ../res/pdf/; mv *.midi ../res/midi/")