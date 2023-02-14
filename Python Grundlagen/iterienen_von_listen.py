list = ['A20b', 'T22a', 'B21c', 'W20b', 'W20a']

anzahl = 0

for zenturie in list:
    if '20' in zenturie:
        anzahl += 1

print(str(anzahl) + ' Zenturien haben im Jahr 2020 begonnen.')