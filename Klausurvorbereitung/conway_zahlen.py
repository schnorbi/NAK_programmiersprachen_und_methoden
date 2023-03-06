list = []
num = 381654729

def conway_check(num):
    dividend = 1000000000
    num_2 = num
    for i in range (1,11):
        if (num // dividend) % i != 0:
            return "Keine Conway-Zahl"
        if num_2 % 10 not in list:
            list.append(num_2 % 10)
            num_2 = num_2 // 10
        else:
            return "Keine Conway-Zahl"
    print(list)
    if len(list) == 10:
        return "Conway-Zahl"
    else:
        return "Keine Conway-Zahl"

print(conway_check(num))