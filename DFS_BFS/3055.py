import sys
from collections import deque

input = sys.stdin.readline

WATER = 1
ANIMAL = 0

def check(x : int, y : int) -> bool:
    return 0 <= x < R and 0 <= y < C

def solution(start, dest, dq):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    dq.append(start)
    visited = [[0] * C for _ in range(R)]
    while dq:
        x, y, kind = dq.popleft()
        if x == dest[0] and y == dest[1]:
            return visited[x][y]
        for gx, gy in zip(dx, dy):
            nx, ny = x+gx, y+gy
            if not check(nx, ny) or visited[nx][ny]:
                continue
            if board[nx][ny] == "*" or board[nx][ny] == "X":
                continue
            
            if kind == WATER and board[nx][ny] == "D":
                continue

            if kind == WATER:
                board[nx][ny] = "*"
                dq.append((nx, ny, WATER))
            else:
                visited[nx][ny] = visited[x][y] + 1
                dq.append((nx, ny, ANIMAL))

    return "KAKTUS"

if __name__ == "__main__":
    R, C = map(int, input().split())
    board = []
    dq = deque([])
    for x in range(R):
        tmp = list(input().rstrip())
        for idx, val in enumerate(tmp):
            if val == "S":
                start = (x, idx, ANIMAL)
            elif val == "D":
                dest = (x, idx)
            elif val == "*":
                dq.append((x, idx, WATER))
        board.append(tmp)
    print(solution(start, dest, dq))
