'''def rec_max_one(list):
    for i in list:
        if i > list[0]:
            list[0] = i
    return list[0]'''

def rec_max_two(list):
    if len(list) > 1:
        if list[0] < list[1]:
            del list[0]
            rec_max_two(list)
        else:
            del list[1]
            rec_max_two(list)
    return list[0]


'''list = [1, 2, 6, 5, 7, 8]
print(rec_max_one(list))'''
list = [1, 2, 8, 5, 7, 8]
print(rec_max_two(list))