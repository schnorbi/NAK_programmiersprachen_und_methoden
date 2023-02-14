number = str(input('Welche Zahl soll umgerechnet werden: '))
#this is a change

def left_number(number_left):
    break_counter = 1
    binare_left = ''

    while break_counter > 0:
        binare_left = str(number_left % 2) + binare_left
        number_left = number_left // 2

        if number_left == 0:
            break_counter = 0

    return binare_left

def right_number(number_right, runs):
    break_counter = 1
    binare_right = ''

    number_right = float('0.' + str(number_right))

    while break_counter > 0:
        number_right = number_right * 2
        if number_right >= 1:
            binare_right = binare_right + '1'
            number_right = number_right - 1
        else:
            binare_right = binare_right + '0'

        runs = runs - 1

        if runs == 0 or number_right == 0:
            break_counter = 0

    return binare_right

if '.' in number:
    runs = int(input('Wie viele Nachkomma berechnungen sollen maximal gemacht werden: '))

    split_number = number.split('.')
    number_left = split_number[0]
    number_right = split_number[1]

    binare = str(left_number(int(number_left))) + '.' + str(right_number(int(number_right), runs))

else:
    binare = str(left_number(int(number)))

print(binare)