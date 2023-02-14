#ist halt ein string
def cross_one(integer):
    crosssum = 0
    for i in integer:
        crosssum += int(i)
    return crosssum

#fucking ineffizient
def cross_two(integer):
    crosssum = 0
    for i in range(0, integer-1):
        crosssum += (integer % 10)
        integer = integer // 10
    return crosssum

#fast af
def cross_three(integer):
    crosssum = 0
    while integer > 0:
        crosssum += (integer % 10)
        integer = integer // 10
    return crosssum

integer = input('Von welcher Zahl soll die Quersumme berechnet werden: ')
print('Quersumme 1 von ' + str(integer) + ' ist ' + str(cross_one(str(integer))))
print('Quersumme 2 von ' + str(integer) + ' ist ' + str(cross_two(int(integer))))
print('Quersumme 3 von ' + str(integer) + ' ist ' + str(cross_three(int(integer))))
