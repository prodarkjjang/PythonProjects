#10 Learn about look and say sequence
# len(a[30]) = ?, i assume is how many numbers
# could be base 3 number, got 1,4,7,49,376
# could be add the individual digit in each numbers,ie 1,2,3,5,8
# fibonaci of a[30] is 2178309 where a[0] = 1 and a[1] = 2
# len(a[30]) = ? what does this mean
# not number of digit -> 7
# not total of each digit -> 30
# not 2178309
# Realise i might totally be off track, partially check solution and saw 'Look and say sequence'
# Look and say sequence for example 11 is 'one 1' and 21 is 'one 2 one 1'

a = [1, 11, 21, 1211, 111221]

def fib(num):
    if num == 0:
        return 1
    elif num == 1:
        return 2
    else:
        return fib(num - 2) + fib(num - 1)

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(30))

total = 0
i = 2178309
while i:
    total += i % 10
    i //= 10

print(total)

# attempt after look and say sequence hint
def lns(num):
    if num == 0:
        return 1
    else:
        res = []
        number = str(lns(num - 1))
        cur = number[0]
        count = 1
        for i in range(1, len(number)):
            if cur == number[i]:
                count += 1
            else:
                res.append(str(count))
                res.append(cur)
                cur = number[i]
                count = 1
        res.append(str(count))
        res.append(cur)
    
    return int("".join(res))

print(lns(0))
print(lns(1))
print(lns(2))
print(lns(3))
print(lns(30))
print(len(str(lns(30))))
