import sys
import math

line = [int(x.strip()) for x in sys.stdin.readline().split(' ')]

def digits_count(num):
    return int(math.floor(math.log10(num))+1)

for t in range(25):
    new_line = []
    for n in line:
        if n == 0:
            new_line.append(1)
            continue

        digits = digits_count(n)
        if digits % 2 == 0:
            half_digits = digits // 2
            new_line.append(n // (10 ** half_digits))
            new_line.append(n % (10 ** half_digits))
            continue

        new_line.append(n * 2024)
    line = new_line
print(len(line))


