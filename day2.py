
reports = []
cnt = 0
with open('day2-in.txt', 'r') as file:
    for line in file:
        report = [int(x) for x in line.strip().split()]
        reports.append(report)

for report in reports:
    safe = True
    is_asc = None
    for i in range(1, len(report)):
        diff = report[i] - report[i-1]
        if diff < -3 or diff == 0 or diff > 3:
            safe = False
            break
        if is_asc is None:
            if diff > 0:
                is_asc = True
            else:
                is_asc = False
        elif (is_asc and diff < 0) or (not is_asc and diff > 0):
            safe = False
            break
    if safe:
        cnt += 1

print(cnt)