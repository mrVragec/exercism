def steps(number):

    if number <= 0:
        # example when argument is zero or a negative integer
        raise ValueError("Only positive integers are allowed")

    n = number
    index = 0
    while (n != 1):
        if(n%2 == 1):
            n = 3 * n + 1
        elif (n % 2 == 0):
            n = n/2
        index += 1
    
    return index
