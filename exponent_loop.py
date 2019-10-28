#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Oct 2019
# This is program loop number exponent


def main():
    # funciton calculates the number squared

    # variable
    answer = 1
    repeater = 0

    # Welcome statement
    print("Welcome, I will give you the square of your number.")
    print("Ex. 2² = 4")
    input("\nPress Enter to continue.")

    # input
    number = int(input("What is your number: "))

    # process
    for repeater in range(number + 1):
        answer = repeater * repeater
        print(str(repeater) + "² = " + str(answer))


if __name__ == "__main__":
    main()
