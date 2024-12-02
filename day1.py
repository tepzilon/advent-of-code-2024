
list_a = []
list_b = []
diff = 0
with open('day1-in.txt', 'r') as file:
    for line in file:
        (a,b) = line.strip().split()
        list_a.append(int(a))
        list_b.append(int(b))
list_a.sort()
list_b.sort()
for i in range(len(list_a)):
    diff += abs(list_a[i] - list_b[i])
print(diff)