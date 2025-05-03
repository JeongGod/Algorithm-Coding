import sys

input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    dp = [1, 2]

    for i in range(2, N):
        dp.append(dp[i-1] + dp[i-2])
    print(dp[N-1] % 10007)