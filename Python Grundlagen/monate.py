print( 'Eingabe MM/JJJJ (bspw. 1/2022): ', end='')
inp = input().split('/')
monat = int(inp[0])
jahr = int(inp[1])

#Aufgabe 4:
match monat:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("Der Monat hat 31 Tage.")
    case 2:
        if ( jahr % 4 == 0 and monat == 2):
            print("Der Monat hat 29 Tage.")
        else:
            print("Der Monat hat 28 Tage.")
    case 4 | 6 | 8 | 9 | 11:
        print("Der Monat hat 30 Tage.")
    case _:
        print("Falsche Eingabe")