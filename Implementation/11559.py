import sys
from collections import deque

input = sys.stdin.readline

X, Y = 6, 12

board = [list(input().rstrip()) for _ in range(Y)]

"""
4개이상이 모이면 터진다.
"""
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]



def search(y, x, val):
    dq = deque([(y, x)])
    flag = False
    visited = set()
    while dq:
        cy, cx = dq.popleft()
        if len(visited) >= 4:
            flag = True
        for i in range(4):
            ny, nx = cy + dx[i], cx + dy[i]
            if 0 <= nx < X and 0 <= ny < Y and board[ny][nx] == val and (ny, nx) not in visited:
                visited.add((ny, nx))
                dq.append((ny, nx))
    if flag:
        return visited
    return set()

def puyopop(_list : set) -> None:
    for x, y in _list:
        board[x][y] = "."

def puyodown() -> None:
    for x in range(X):
        dq = deque([])
        for y in range(Y):
            if board[y][x] == ".":
                continue
            dq.append(board[y][x])
            board[y][x] = "."
        for y in range(Y-len(dq), Y):
            board[y][x] = dq.popleft()

answer = 0
while True:
    puyo = set()
    for i in range(Y):
        for j in range(X):
            if board[i][j] == "." or (i, j) in puyo:
                continue
            puyo |= search(i, j, board[i][j])
    
    puyopop(puyo)
    puyodown()
    
    if not puyo:
        break
    answer += 1

print(answer)