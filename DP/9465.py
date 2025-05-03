import sys

input = sys.stdin.readline

def sticker(n, board):
    sum_max = [[0] * n for _ in range(2)]

    sum_max[0][0] = board[0][0]
    sum_max[1][0] = board[1][0]
    sum_max[0][1] = board[1][0] + board[0][1]
    sum_max[1][1] = board[0][0] + board[1][1]

    for i in range(2, n):
        sum_max[0][i] = max(sum_max[1][i-1] + board[0][i], max(sum_max[0][i-2], sum_max[1][i-2]) + board[0][i])
        sum_max[1][i] = max(sum_max[0][i-1] + board[1][i], max(sum_max[0][i-2], sum_max[1][i-2]) + board[1][i])

    return max(sum_max[0][n-1], sum_max[1][n-1])

if __name__ == "__main__":
    TC = int(input())

    for _ in range(TC):
        BOARD = []
        N = int(input())
        BOARD.append([*map(int, input().split())])
        BOARD.append([*map(int, input().split())])
        if (N == 1):
            print(max(BOARD[0][0], BOARD[1][0]))
        else:
            print(sticker(N, BOARD))
