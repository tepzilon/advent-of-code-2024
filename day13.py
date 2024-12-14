import sys
import re

lines = sys.stdin.readlines()

sum = 0
for i in range(0, len(lines), 4):
    m = re.match(r"Button A: X\+(\d+), Y\+(\d+)", lines[i])
    btn_a_step_x = int(m.group(1))
    btn_a_step_y = int(m.group(2))

    m = re.match(r"Button B: X\+(\d+), Y\+(\d+)", lines[i+1])
    btn_b_step_x = int(m.group(1))
    btn_b_step_y = int(m.group(2))

    m = re.match(r"Prize: X=(\d+), Y=(\d+)", lines[i+2])
    prize_x = int(m.group(1))
    prize_y = int(m.group(2))

    # print(btn_a_step_x, btn_a_step_y, btn_b_step_x, btn_b_step_y, prize_x, prize_y)

    cost = 0
    for times_a in range(0, 101):
        for times_b in range(0, 101):
            if btn_a_step_x * times_a + btn_b_step_x * times_b == prize_x and btn_a_step_y * times_a + btn_b_step_y * times_b == prize_y:
                cost = times_a * 3 + times_b
                break
    sum += cost

print(sum)
