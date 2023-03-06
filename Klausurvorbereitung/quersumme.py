num = 371

def cross(num):
    crosssum = 0
    while num > 0:
        num_part = num % 10
        num = num // 10
        crosssum = crosssum + num_part

    return crosssum

print(cross(num))