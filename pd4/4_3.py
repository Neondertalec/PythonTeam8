import regex as rx
from pathlib import Path
import requests

base = Path(__file__).resolve().parent
git_base = Path(__file__).parent

handle_en = None
handle_lv = None
try:
    handle_en = open(base/'EN.txt', 'r')
    handle_lv = open(base/'LV.txt', 'r')
except:
    handle_en = requests.get('https://raw.githubusercontent.com/Neondertalec/PythonTeam8/main/pd4/EN.txt').text
    handle_lv = requests.get('https://raw.githubusercontent.com/Neondertalec/PythonTeam8/main/pd4/LV.txt').text

preload = 'abcdefghijklmnopqrstuvwxyz'

total_letters_en = 0
total_letters_lv = 0
eng_histogram = []
lv_histogram = []

for letter in rx.findall('[a-z]', preload):
    eng_histogram.append((letter, 0))
    lv_histogram.append((letter, 0))

for line in handle_en:
    line = rx.findall('[a-z]', line.lower())
    for letter in line:
        total_letters_en += 1
        eng_histogram = [(l, c + 1 if l == letter else c) for (l, c) in eng_histogram]
    

eng_histogram = [(count / total_letters_en, letter) for (letter, count) in eng_histogram]
eng_histogram = [(letter, percentage) for (percentage, letter) in sorted(eng_histogram, reverse= True)]

for line in handle_lv:
    line = rx.findall('[a-z]', line.lower())
    for letter in line:
        total_letters_lv += 1
        lv_histogram = [(l, c + 1 if l == letter else c) for (l, c) in lv_histogram]

lv_histogram = [(count / total_letters_en, letter) for (letter, count) in lv_histogram]
lv_histogram = [(letter, percentage) for (percentage, letter) in sorted(lv_histogram, reverse= True)]

combined_hist = [(en, lv_histogram[i]) for i, en in enumerate(eng_histogram)]

print('English'.ljust(15) + 'Latvian')

for ((letter, percentage), (letter_lv, perc_lv)) in combined_hist:
    print(f'{letter}: {percentage:.3f}%'.ljust(15) + f'{letter_lv}: {perc_lv:.3f}%')