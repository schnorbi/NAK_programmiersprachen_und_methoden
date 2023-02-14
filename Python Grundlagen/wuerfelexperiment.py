import random
import matplotlib.pyplot as plt

auswertung = {}
gesamtwuerfelzahl = 0

n = int(input('Anzahl der Würfel: '))

for i in range(1000):
    for j in range(n):
        zahl = random.randint(1, 6)
        gesamtwuerfelzahl += zahl
        if gesamtwuerfelzahl in auswertung:
            auswertung[gesamtwuerfelzahl] += 1
        else:
            auswertung[gesamtwuerfelzahl] = 1
    gesamtwuerfelzahl = 0

print(auswertung)

plt.bar(*zip(*auswertung.items()))
plt.show()