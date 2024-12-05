# idk why this is working

lines = []
with open('day5-in.txt', 'r') as file:
    lines = file.readlines()
read_second_section = False
rules = set()
failed = []
sum = 0

for line in lines:
    if line == '\n':
        read_second_section = True
        continue
    if read_second_section:
        update = [int(x.strip()) for x in line.split(',')]
        len_update = len(update)
        assert len_update % 2 == 1
        ok = True
        for i in range(len_update):
            for j in range(0,i):
                if (update[i],update[j]) in rules:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            failed.append(update)
    else:
        (x,y) = (int(x.strip()) for x in line.split('|'))
        rules.add((x,y))

for update in failed:
    len_update = len(update)
    correct = False
    while not correct:
      correct = True
      for i in range(len_update):
          for j in range(0, i):
            if (update[i],update[j]) in rules:
                update[i],update[j] = update[j],update[i]
                correct = False
                break
    if correct:
        sum += update[len_update // 2]

print(sum)