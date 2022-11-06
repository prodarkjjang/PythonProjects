# Write a function on a parking fee system.
# 1. First 2 hours is RM3
# 2. Every subsequent hour is RM1
# 3. The fee is capped at RM15

def calculateFee(hours):
    if hours <= 2:
        return 3
    else:
        fee = (hours - 2) + 3
        return fee if fee <= 15 else 15


io = {0 : 3, 1 : 3, 2 : 3, 3 : 4, 4 : 5, 5 : 6, 6 : 7, 7 : 8, 8 : 9, 9 : 10, 10 : 11, 11 : 12, 12 : 13, 13 : 14, 14 : 15, 15 : 15, 16 : 15}

for item in io.items():
    assert calculateFee(item[0]) == item[1], str(item[0]) + " should return " + str(item[1])
