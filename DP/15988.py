import sys

input = sys.stdin.readline

DIV = 1_000_000_009

def solution(n : int) -> int:
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, n+1):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % DIV
    return dp

if __name__ == "__main__":

    TC = int(input())
    li = [int(input()) for _ in range(TC)]
    result = solution(max(li))
    for i in li:
        print(result[i])
