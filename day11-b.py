import sys
import math

line = [int(x.strip()) for x in sys.stdin.readline().split(' ')]

bucket = {}

def digits_count(num):
    return int(math.floor(math.log10(num))+1)

for n in line:
    bucket[n] = bucket[n]+1 if n in bucket else 1


for t in range(75):
    new_bucket = {}
    for n, cnt in bucket.items():
        if n == 0:
            new_bucket[1] = new_bucket[1] + cnt if 1 in new_bucket else cnt
            continue

        digits = digits_count(n)
        if digits % 2 == 0:
            half_digits = digits // 2
            first_half = int(n // (10 ** half_digits))
            second_half = int(n % (10 ** half_digits))
            new_bucket[first_half] = new_bucket[first_half] + cnt if first_half in new_bucket else cnt
            new_bucket[second_half] = new_bucket[second_half] + cnt if second_half in new_bucket else cnt
            continue

        n_times_1024 = n * 2024
        new_bucket[n_times_1024] = new_bucket[n_times_1024] + cnt if n_times_1024 in new_bucket else cnt
    bucket = new_bucket

sum = 0
for n, cnt in bucket.items():
    sum += cnt

print(sum)


