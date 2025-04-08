import re
import time

# Input- und Output-Dateien
input_file = 'av_logexport-250408-1_details.log'
output_file = 'output-'+time.strftime("%Y%m%d-%H%M%S")+'.txt'

# Set für eindeutige Kombinationen
entries = set()

# Regex erlaubt Buchstaben, Zahlen, Unterstrich, Punkt, Bindestrich, Umlaute, ß
pattern = re.compile(r"im Besitz von ([\w\.\-äöüÄÖÜß]+) auf ([\w\.\-äöüÄÖÜß]+) wurde auf ([\w\.\-äöüÄÖÜß]+)")

# Datei lesen und Zeilen parsen
with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        match = pattern.search(line)
        if match:
            user, pc, printer = match.groups()
            entries.add(f"{user} | {pc} | {printer}")
            print(f"User: {user} | Client: {pc} | Printer: {printer}")

# Ausgabe schreiben
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('User | Client | Printer\n')
    for entry in sorted(entries):
        f.write(entry + '\n')

print(f"{len(entries)} eindeutige Einträge wurden in '{output_file}' geschrieben.")
