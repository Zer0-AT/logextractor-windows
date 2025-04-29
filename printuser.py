import re
import time
import os

# Input- und Output-Dateien
input_file = 'avex_250417.log'
output_dirname = 'output'
output_filename = 'output-printuser-'+time.strftime("%Y%m%d-%H%M%S")+'.txt'
output_file = os.path.join(output_dirname, output_filename)

os.makedirs(output_dirname, exist_ok=True)

# Set für eindeutige Kombinationen
entries = set()

# Regex erlaubt Buchstaben, Zahlen, Unterstrich, Punkt, Bindestrich, Umlaute, ß, ...
pattern = re.compile(r"im Besitz von ([\w\.\- $äöüÄÖÜß]+) auf ([\w\.\- $äöüÄÖÜß]+) wurde auf ([\w\.\- $äöüÄÖÜß]+) über Port")

# Datei lesen und Zeilen parsen
with open(input_file, 'r', encoding='utf-8') as f:
    print(f"User | Client | Printer")
    matches = 0
    for line in f:
        match = pattern.search(line)
        if match:
            user, pc, printer = match.groups()
            entries.add(f"{user} | {pc} | {printer}")
            print(f"{user} | {pc} | {printer}")
            matches += 1
    print(f"\n\n{matches} Einträge gefunden.")

# Ausgabe schreiben
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('User | Client | Printer\n')
    for entry in sorted(entries):
        f.write(entry + '\n')

print(f"{len(entries)} eindeutige Einträge wurden in '{output_file}' geschrieben.")
