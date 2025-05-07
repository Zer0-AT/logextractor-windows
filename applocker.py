import re
import time
import os

# Input- und Output-Dateien
input_file = 'wcex_250429.log'
output_dirname = 'output'
output_filename = 'output-applocker-'+time.strftime("%Y%m%d-%H%M%S")+'.txt'
output_file = os.path.join(output_dirname, output_filename)

os.makedirs(output_dirname, exist_ok=True)

#Fromat
output_header = 'User | Client | PolicyName | Path\Software'
domain = '.domain.local'

# Set für eindeutige Kombinationen
entries = set()

# Regex erlaubt Buchstaben, Zahlen, Unterstrich, Punkt, Bindestrich, Umlaute, ß, ...
pattern = re.compile(
    rf"Benutzer:.*?(.*?)\n.*?<Computer>(.*?)\b{re.escape(domain)}\b.*?<PolicyName>(.*?)</PolicyName>.*?<FilePath>(.*?)</FilePath>",
    re.DOTALL
)
# Datei lesen und Zeilen parsen
with open(input_file, 'r', encoding='utf-8') as f:
    print(f"{output_header}")
    content = f.read()
    matches_i = 0
    matches = pattern.findall(content)
    for match in matches:
        entries.add(" | ".join(m.strip() for m in match))
        print(f"{' | '.join(m.strip() for m in match)}")
        matches_i += 1
    print(f"\n\n{matches_i} Einträge gefunden.")

# Ausgabe schreiben
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(output_header+"\n")
    for entry in sorted(entries):
        f.write(entry + '\n')

print(f"{len(entries)} eindeutige Einträge wurden in '{output_file}' geschrieben.")
