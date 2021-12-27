"""
1. 첫번째 동전만 사용했을 경우 가능한 경우의 수를 기억한다.
2. 첫번째 + 두번째를 사용했을 경우의 경우의 수를 기억한다.
3. K까지 반복
"""
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coins = list(int(input()) for _ in range(N))
dp = [0] * 100001

for coin in coins:
    dp[coin] += 1
    for i in range(1, K+1):
        if i - coin >= 0:
            dp[i] += dp[i-coin]
print(dp[K])
