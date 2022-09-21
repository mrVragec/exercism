def square_of_sum(number):

    sum = 0
    for i in range(0, number):
        sum += i+1

    return pow(sum, 2)

def sum_of_squares(number):
    
    sum = 0
    for i in range(0, number):
        sum += pow(i+1, 2)

    return sum

def difference_of_squares(number):
    return square_of_sum(number=number) - sum_of_squares(number)
