import sys

lines = sys.stdin.readlines()

patterns = [p.strip() for p in lines[0].split(',')]
texts = [t.strip() for t in lines[2:]]


def num_possible(text, patterns):
    dp = [0 for i in range(len(text)+1)]
    dp[0] = 1
    for i in range(1, len(text)+1):
        for p in patterns:
            if i-len(p) >= 0 and text[i-len(p):i] == p:
                dp[i] = dp[i] + dp[i-len(p)]
    return dp[len(text)]

sum = 0
for t in texts:
    sum += num_possible(t, patterns)

print(sum)