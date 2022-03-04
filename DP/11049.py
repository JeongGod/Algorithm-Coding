import sys

input = sys.stdin.readline

def calc(start, mid, end):
    return pro[start][mid][0] * pro[start][mid][1] * pro[mid+1][end][1]

def solution(pro):
    """
    dp[i][j] = min(dp[i][i] + dp[i+1][j], dp[i][i+1] + dp[i+2][j] ... dp[i][i+j-1] + dp[j][j])
    """
    n = len(pro)
    dp = [[0] * n for _ in range(n)]
    for r in range(1, n):
        for start in range(n-r):
            end = start + r
            dp[start][end] = sys.maxsize
            for mid in range(start, end):

                pro[start][end] = [pro[start][mid][0], pro[mid+1][end][1]]
                dp[start][end] = min(dp[start][end], dp[start][mid] + dp[mid+1][end] + calc(start, mid, end))
    return dp[0][n-1]

if __name__ == "__main__":
    N = int(input())
    pro = [[[] for _ in range(N)] for _ in range(N)]
    for idx in range(N):
        pro[idx][idx] = list(map(int, input().split()))
    
    print(solution(pro))
