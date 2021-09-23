import sys

input = sys.stdin.readline

N = int(input())
health = sorted(list(map(int, input().split())))
ans = 0
if len(health) % 2 == 1:
    ans = health.pop()

for a, b in zip(health[::-1], health):
    ans = max(ans, a+b)
print(ans)
