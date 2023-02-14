print( 'Anzahl der Zeilen der Pyramide: ', end='')
n = int(input())

for i in range(n):
    print(' '*(n-1-i) + '*' + '*'*(i*4))