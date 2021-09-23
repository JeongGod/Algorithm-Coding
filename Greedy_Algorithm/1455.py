import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = []
for i in range(N):
    board.append(list(map(lambda x : 1 if x == "1" else -1, list(input().rstrip()))))


def flip(x, y):
    for i in range(x+1):
        for j in range(y+1):
            board[i][j] *= -1
ans = 0
for i in range(N-1, -1, -1):
    for j in range(M-1, -1, -1):
        if board[i][j] == 1:
            ans += 1
            flip(i, j)

print(ans)
