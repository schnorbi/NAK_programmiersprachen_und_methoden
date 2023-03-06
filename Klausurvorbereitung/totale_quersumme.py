num = 55

def cross(num):
    crosssum = 0
    while num > 0:
        num_part = num % 10
        num = num // 10
        crosssum = crosssum + num_part

    return crosssum

def cross_total(num):
    while num > 9:
        num = cross(num)
    return num


print(cross_total(num))