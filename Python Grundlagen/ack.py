n = int(input('Number n: '))
m = int(input('Number m: '))

recursion = [0]

def ack(number_n, number_m):
    global recursion
    recursion[0] = recursion[0] + 1
    print(recursion[0])
    if number_n == 0:
        return number_m + 1

    elif number_m == 0 and number_n > 0:
        return ack(number_n - 1, 1)

    else:
        return ack(number_n - 1, ack(number_n, number_m - 1))


print(ack(n, m))

