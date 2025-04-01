from googletrans import Translator

# Read the VTT file
with open('st-uacxdkki.en.srt.vtt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Initialize the translator
translator = Translator()

# Translate each line (this assumes text appears after timestamps)
for i, line in enumerate(lines):
    if '-->' not in line:  # Skip lines with timestamps
        lines[i] = translator.translate(line.strip(), src='en', dest='es').text + '\n'

# Write the translated content back to a new VTT file
with open('st-uacxdkki.es.srt.vtt', 'w', encoding='utf-8') as file:
    file.writelines(lines)