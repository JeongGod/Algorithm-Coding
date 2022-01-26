import sys

input = sys.stdin.readline

def solution(n):
    if n[0] == "0":
        return 0

    dp = [0] * (len(n) + 1)
    dp[0], dp[1] = 1, 1
    for idx in range(2, len(n)+1):
        val = int(n[idx-2] + n[idx-1])
        if 0 < int(n[idx-1]) <= 9:
            dp[idx] = dp[idx-1]
        if 10 <= val <= 26:
            dp[idx] += dp[idx-2]
        dp[idx] %= 1000000
        
    return dp[len(n)]
if __name__ == "__main__":
    N = input().rstrip()
    print(solution(N))
