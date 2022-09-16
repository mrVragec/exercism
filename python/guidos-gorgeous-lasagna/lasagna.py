"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 20

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """"Calculate the preparation time in minutes

    :param number_of_layers: int - numbers of layers to be added to lasagna
    :return: int - time needed to prepare lasagna with desired number of layers
    """
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """""Calculate the elapsed time in minutes based on the number of layers and elapsed bake time

    :param number_of_layers: int - number of layers to be added to lasagna.
    :elapsed_bake_time: int - baking time already elapsed.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
