#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastD = number % 10
    if lastD > 5:
        print(f"Last digit of {number} is {lastD} and is greater than 5")
    if lastD == 0:
        print(f"Last digit of {number} is {lastD} and is 0")
    if lastD < 6 and lastD != 0:
        print(f"Last digit of {number} is {lastD} and is less than 6 and not 0")
else:
    lastD = -(-number % 10)
    print(f"Last digit of {number} is {lastD} and is less than 6 and not 0")
