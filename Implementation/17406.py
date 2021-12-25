import copy
import sys
from itertools import permutations

input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
info = [list(map(int, input().split())) for _ in range(K)]
ans = sys.maxsize


def rotate(sx, sy, tx, ty):
    tmp = board[sx][sy]
    # 아래
    for i in range(sx, tx):
        board[i][sy] = board[i+1][sy]
    # 오른
    for j in range(sy, ty):
        board[i+1][j] = board[i+1][j+1]
    # 위
    for i in range(tx, sx, -1):
        board[i][j+1] = board[i-1][j+1]
    # 왼쪽
    for j in range(ty, sy+1, -1):
        board[i-1][j] = board[i-1][j-1]
    board[sx][sy+1] = tmp


for per in permutations(info, len(info)):
    tmp = copy.deepcopy(board)
    for r, c, s in per:
        r, c = r-1, c-1
        for i in range(1, s+1):
            rotate(r-i, c-i, r+i, c+i)

    for line in board:
        ans = min(ans, sum(line))
    board = tmp
print(ans)
