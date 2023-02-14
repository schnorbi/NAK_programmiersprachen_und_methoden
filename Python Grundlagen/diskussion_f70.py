def berechnung_summe(untere_grenze, obere_grenze):
    summe = 0
    for i in range(untere_grenze, obere_grenze + 1):
        summe += i
    return summe

print(berechnung_summe(10,20))

print(berechnung_summe(4,10))