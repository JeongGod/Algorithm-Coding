import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]

ans = 0
for c in coin[::-1]:
    if K == 0:
        break
    while K - c >= 0:
        K -= c
        ans += 1
print(ans)
