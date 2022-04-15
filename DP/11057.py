import sys

input = sys.stdin.readline
DIV = 10007

if __name__ == "__main__":
    N = int(input())
    """
    dp[i][k] = i로 끝나는 k자릿수를 가졌을 때의 경우의 수
    """
    dp = [[0] * (N+1) for _ in range(11)]
    # 처음 첫 자릿수
    for i in range(10):
        dp[i][1] = 1
    dp[10][1] = 10
    before = dp[10][1]
    for k in range(2, N+1):
        # 0으로 시작했던 경우에는 모두 가능하다.
        tmp = before
        dp[0][k] = before
        for i in range(1, 10):
            # 전체 합에서
            dp[i][k] = dp[i-1][k] - dp[i-1][k-1]
            tmp += dp[i][k]
            tmp %= DIV
        before = tmp
        dp[10][k] = tmp

    print(dp[10][N])
