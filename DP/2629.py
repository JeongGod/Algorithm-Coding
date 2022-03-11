import sys

input = sys.stdin.readline

def make_dp(chus : list[int]) -> list[list[int]]:
    """
    i : 추의 개수, j : 만들 수 있는 무게
    i번째의 추(무게 : c)를 사용해서 j의 무게를 만들 수 있는가
    dp[i][j] = dp[i-1][j-c] || dp[i-1][j] || dp[i-1][j+c]
    """
    dp = [[False] * 40001 for _ in range(N+1)]
    for i in range(1, N+1):
        dp[i][chus[i-1]] = True
    
    for i in range(2, N+1):
        c = chus[i-1]
        for j in range(1, 40001-c):
            dp[i][j] |= dp[i-1][abs(j-c)] or dp[i-1][j] or dp[i-1][j+c]
    
    return dp


if __name__ == "__main__":
    N = int(input())
    chus = list(map(int, input().split()))
    dp = make_dp(chus)

    M = int(input())
    flag = False
    check_chus = list(map(int, input().split()))
    for ch_idx in range(M):
        for i in range(1, N+1):
            if dp[i][check_chus[ch_idx]]:
                flag = True
                break
        if flag:
            print("Y", end = " ")
        else:
            print("N", end = " ")
        flag = False

    print("")
