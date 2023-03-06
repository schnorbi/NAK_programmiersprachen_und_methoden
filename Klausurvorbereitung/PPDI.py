num = 371

def is_ppdi(num):
    ppdi = 0
    start_num = num

    for i in range(0,3):
        num_part = num % 10
        num = num // 10
        ppdi = ppdi + num_part**3

    return ppdi == start_num


for i in range(0,100000000):
    if is_ppdi(i) == True:
        print(i)
