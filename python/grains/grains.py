def square(number):
    if number not in range(1, 65):
        raise ValueError("square must be between 1 and 64")

    return pow(2, (number - 1))


def total():
    sum = 0
    for i in range(1, 65):
        sum += square(i)
    return sum

# 1 2 3 4 5   6  7   8   9 10
# 1 2 4 8 16 32 64 128 256 512

