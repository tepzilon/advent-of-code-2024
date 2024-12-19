import sys

lines = sys.stdin.readlines()

patterns = [p.strip() for p in lines[0].split(',')]
texts = [t.strip() for t in lines[2:]]


def possible(text, patterns):
    dp = [False for i in range(len(text)+1)]
    dp[0] = True
    for i in range(1, len(text)+1):
        for p in patterns:
            if text[i-len(p):i] == p:
                dp[i] = dp[i] or dp[i-len(p)]
    return dp[len(text)]

count = 0
for t in texts:
    if possible(t, patterns):
        count += 1

print(count)