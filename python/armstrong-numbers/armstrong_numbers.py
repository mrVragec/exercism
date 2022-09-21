def is_armstrong_number(number):

    sum = 0
    str_number = str(number)
    str_len = len(str_number)

    for i in range(0, str_len):
        sum += pow(int(str_number[i]), str_len)

    return sum == number
