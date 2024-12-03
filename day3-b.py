import re
content = ""
with open('day3-in.txt') as f:
    content = f.read()
sum = 0
matches = re.findall(r"(do\(\))|(don\'t\(\))|(mul\(([0-9]+),([0-9]+)\))", content)
do = True
for match in matches:
    if match[0] != '':
        do = True
    if match[1] != '':
        do = False
    if match[2] != '':
        if do:
            sum += int(match[3])*int(match[4])
print(sum)