import sys

input = sys.stdin.readline
# 최소 횟수를 출력해라.
N = int(input())
di = dict()
ans = 0
for _ in range(N):
    cow, cur = map(int, input().split())
    before = di.get(cow)
    if before is None:
        di[cow] = cur
    else:
        if before != cur:
            di[cow] = cur
            ans += 1
print(ans)
