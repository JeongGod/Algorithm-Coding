# dp
import sys

input = sys.stdin.readline

N = int(input())
dp = [sys.maxsize]*100002
dp[2], dp[4], dp[5] = 1, 2, 1

for i in range(6, N+1):
    dp[i] = min(dp[i-2], dp[i-5]) + 1

print(dp[N] if dp[N] != sys.maxsize else -1)

# greedy
import sys

input = sys.stdin.readline

N = int(input())
for i in range(N // 5, -1, -1):
    tmp = N - (5*i)
    if tmp%2 == 0:
        print(i + (tmp // 2))
        exit()
print(-1)
