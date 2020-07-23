"""The formula for Luhn's Algorithm says :
1. From the rightmost digit (excluding the check digit) and moving left, double the value of every second digit.
The check digit is neither doubled nor included in this calculation; the first digit doubled is the digit located
immediately left of the check digit. If the result of this doubling operation is greater than 9 (e.g., 8 × 2 = 16),
then add the digits of the result (e.g., 16: 1 + 6 = 7, 18: 1 + 8 = 9)
Take the sum of all the digits.
If the total modulo 10 is equal to 0 (if the total ends in zero) then the number is valid according to the Luhn formula;
otherwise it is not valid
For Example:
4012888888881881
Sum of odd places digits : 43
sum of double of  even places digits : even_digits : [8, 1, 8, 8, 8, 8, 1, 4]  so sum of the double of every digit :
7 + 2 + 7 + 7 + 7 + 7 + 2 + 8 = 47
and totalsum = sum of odd places digits : 43 + the above (47) = 90 for which module is 0, hence the card is valid!."""

import re


def luhn_algorithm(card_number):
    def digits_of(n):
        return [int(i) for i in str(n)]

    digits = digits_of(card_number)
    # Odd digits from rightmost
    odd_digits = digits[-1::-2]
    # Even digits form rightmost
    even_digits = digits[-2::-2]
    checksum = 0
    # sum of odd digits
    checksum += sum(odd_digits)

    # With checksum = sum of odd digits + sum of double of even digits
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    if checksum % 10 != 0:
        print("INVALID")
        exit()

    # Check if AMEX
    if len(card_number) == 15:
        if card_number[0] == "3" and re.search("[47]", card_number[1]):
            print("AMEX")
            exit()
        else:
            print("INVALID")
            exit()

    # Check if MasterCard or 16-digit VISA
    if len(card_number) == 16:
        if card_number[0] == "4":
            print("VISA")
            exit()
        elif card_number[0] == "5" and re.search("[12345]", card_number[1]):
            print("MASTERCARD")
            exit()
        else:
            print("INVALID")
            exit()

    # Check if 13-digit VISA
    if len(card_number) == 13 and card_number[0] == "4":
        print("VISA")
        exit()
    else:
        print("INVALID")
        exit()


luhn_algorithm(input("Number: "))
