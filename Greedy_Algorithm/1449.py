import sys

input = sys.stdin.readline

N, L = map(int, input().split())
water = sorted(list(map(int, input().split())))

guard = set()
ans = 0
for i in water:
    if i not in guard:
        guard |= {*[val for val in range(i, i+L)]}
        ans += 1
print(ans)
