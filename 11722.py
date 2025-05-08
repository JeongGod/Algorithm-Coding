import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    A = [*map(int, input().split())]

    dp = [1] * N
    for i in range(N):
        for j in range(i+1, N):
            if A[i] > A[j]:
                dp[j] = max(dp[i] + 1, dp[j])
    print(max(dp))