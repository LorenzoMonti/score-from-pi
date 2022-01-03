import os
import sys
import Utils


if __name__ == '__main__':
    
    """ 
    Lilypond syntax:
        - diesis: is
        - flat: es
    """
    
    if len(sys.argv) != 3:
        # sheet = 0, tab = 1, sheet+tab = 2
        print('USAGE: generate_sheet.py filename sheet')
        sys.exit(1)

    filename = "../res/lilypond/" + sys.argv[1] + ".ly"
    sheet = sys.argv[2]
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
        Utils.write_sheet(f, notes, sheet)
        

    os.system("lilypond " + filename) # on bash
    os.system("mv *.pdf ../res/pdf/; mv *.midi ../res/midi/")