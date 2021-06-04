#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: June 2021
# This program finds the smallest number among random numbers

import random


def min_of_numbers(numbers):
    # this function finds the max value of the list
    temp_min = numbers[0]

    for loop_counter in numbers:
        if loop_counter <= temp_min:
            temp_min = loop_counter

    return temp_min


def main():
    # this function generates random numbers and calls another function

    # list declaration
    numbers = []

    # process -- generate numbers
    for loop_counter in range(0, 10):
        single_number = random.randint(1, 100)
        numbers.append(single_number)
    print("The numbers are {0}".format(numbers))  # output
    minimum = min_of_numbers(numbers)  # call function
    print("The smallest number is {0}\nDone.".format(minimum))  # output


if __name__ == "__main__":
    main()
