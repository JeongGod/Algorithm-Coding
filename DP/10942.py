import sys

input = sys.stdin.readline

def make_dp(n : int, nums : list[int]) -> list[list[int]]:
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    for i in range(n-1):
        if nums[i] == nums[i+1]:
            dp[i][i+1] = True
    
    for mid in range(2, n):
        for start in range(n-mid):
            end = start + mid
            if nums[start] == nums[end]:
                dp[start][end] = dp[start+1][end-1]
            else:
                dp[start][end] = False

    return dp

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    M = int(input())
    dp = make_dp(N, nums)
    for _ in range(M):
        start, end = map(int, input().split())
        print(1 if dp[start-1][end-1] else 0)
