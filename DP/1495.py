import sys

input = sys.stdin.readline

N, S, M = map(int, input().split())
volumes = list(map(int, input().split()))

dp = [set() for _ in range(N+1)]
dp[0].add(S)
for idx in range(1, N+1):
    for val in dp[idx-1]:
        x, y = val + volumes[idx-1], val - volumes[idx-1]
        if 0 <= x <= M:
            dp[idx].add(x)
        if 0 <= y <= M:
            dp[idx].add(y)
print(max(dp[N]) if dp[N] else -1)
