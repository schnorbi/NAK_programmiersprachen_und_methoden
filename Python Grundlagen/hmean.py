a = [1, 2, 3, 4]

def hmean(a):
    hmean_summe = 0
    for i in a:
        hmean_summe += (1/i)
    return len(a)/hmean_summe

print(hmean(a))