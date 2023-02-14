import time
import sys
sys.set_int_max_str_digits(1000000000)

#n = int(input('Welche Fibunacci-Zahl soll berechnet werden: '))
n = 500000

start = time.time()

fib_one = 0
fib_two = 1

for i in range(n-2):
    new_fib = fib_one + fib_two
    fib_one = fib_two
    fib_two = new_fib

end = time.time()
print(fib_two)
print(f'{end - start} Sekunden')