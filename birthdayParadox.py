# Birthday Paradox states that there is more than 50% chance that someone will have matching birthdays in a group of 23 ppl

import random
import math

def BirthdayMatch(person, groups):
    pairs = int(math.factorial(person) / (math.factorial(groups) * math.factorial(person - groups)))
    for i in range(pairs):
        date1 = random.randint(1, 365)
        date2 = random.randint(1, 365)

        if date1 == date2:
            return True

    return False

def SuccessPercentage(person, group, count):
    chance = [0, 0]
    for i in range(count):
        if BirthdayMatch(person, group):
            chance[0] += 1
        else:
            chance[1] += 1

    percentage = chance[0] /(chance[0] + chance[1]) * 100
    return str(percentage) + "%"

for i in range(10):
    print(SuccessPercentage(23, 2, 1000))