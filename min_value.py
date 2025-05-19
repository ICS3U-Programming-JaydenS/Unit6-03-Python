#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: May 17, 2025
# This code finds the min value out of 10 random numbers


import random

import constants


def min_num_finder(numbers):
    # Set min num to the first number in the list
    min_num = numbers[0]
    # Checks which number is smallest out of the 10 nums
    for counter in numbers:
        # What happens if they are smaller
        if min_num > counter:
            min_num = counter

        # If not use a continue statement to keep it going
        else:
            continue
    return min_num


def main():
    # Set the list
    values = []

    # Gets the random numbers
    for counter in range(0, 10, 1):
        random_number = random.randint(constants.MIN_NUM, constants.MAX_NUM)
        values.append(random_number)
        print(counter, "number:", random_number)

    # Calls function that finds the min value
    min_num = min_num_finder(values)

    # Displays the max value
    print("The min value is", min_num)


if __name__ == "__main__":
    main()
