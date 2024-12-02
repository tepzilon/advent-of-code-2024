count = {}
sum = 0
list_a = []
list_b = []
with open('day1-in.txt', 'r') as file:
    for line in file:
        (a,b) = line.strip().split()
        list_a.append(int(a))
        list_b.append(int(b))

for x in list_b:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1

for x in list_a:
    if x in count:
        sum += count[x] * x

print(sum)