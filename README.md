# SCORE FROM PI

### USAGE
First of all you need to generate pi numbers, the `generate_pi.py` script will be for you (inside src/ folder).

`USAGE: generate_pi.py ndigits outfile`

After that, you can generate score from pi number based on your favourite key. Inside config/ folder you can find `key.json` file, fill it in by entering your key. Launch `generate_sheet.py` script in order to generate PDF and MIDI file (in folder res/pfd/ and res/midi/ respectively).

`USAGE: generate_score.py filename score`

you can choose to generate the score by adding 0 in the last parameter, otherwise 1 if you want the tablature.

### WHAT'S NEEDED
you only need [Lilypond](https://lilypond.org/) installed on your system to get these scripts to work.
