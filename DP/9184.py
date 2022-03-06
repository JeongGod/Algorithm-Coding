import sys

input = sys.stdin.readline

def make_arr(a : int, b : int, c : int) -> list[list[list[int]]]:
    dp = [[[1] * (a+1) for _ in range(b+1)] for _ in range(c+1)]
    for i in range(1, a+1):
        for j in range(1, b+1):
            for k in range(1, c+1):
                if a < b < c:
                    dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] + dp[i][j-1][k]
                else:
                    dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]
    return dp

if __name__ == "__main__":
    dp = make_arr(20, 20, 20)
    while True:
        a, b, c = map(int, input().split())
        if a == -1 and b == -1 and c == -1:
            break
        elif a <= 0 or b <= 0 or c <= 0:
            print(f"w({a}, {b}, {c}) = {1}")
        elif a > 20 or b > 20 or c > 20:
            print(f"w({a}, {b}, {c}) = {dp[20][20][20]}")
        else:
            print(f"w({a}, {b}, {c}) = {dp[a][b][c]}")
