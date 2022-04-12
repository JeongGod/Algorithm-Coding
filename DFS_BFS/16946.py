import sys
from collections import deque

input = sys.stdin.readline


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def check(x, y):
    return 0 <= x < N and 0 <= y < M

def bfs(board, x, y, t):
    dq = deque([(x, y)])
    cnt = 1
    while dq:
        cx, cy = dq.popleft()
        for gx, gy in zip(dx, dy):
            nx, ny = cx + gx, cy + gy
            if not check(nx, ny) or board[nx][ny] == 1:
                continue
            if visited[nx][ny] != 0:
                continue
            visited[nx][ny] = t
            dq.append((nx, ny))
            cnt += 1
    
    return cnt
    

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().rstrip())) for _ in range(N)]

    
    visited = [[0] * M for _ in range(N)]
    t = 1
    island = dict()
    island[0] = 0
    for x in range(N):
        for y in range(M):
            if visited[x][y] != 0:
                continue
            if board[x][y] == 0:
                visited[x][y] = t
                island[t] = bfs(board, x, y, t)
                t += 1

    for x in range(N):
        for y in range(M):
            if board[x][y] == 1:
                islands = set()
                result = 1
                for gx, gy in zip(dx, dy):
                    nx, ny = x + gx, y + gy
                    if not check(nx, ny):
                        continue
                    island_name = visited[nx][ny]
                    if island_name in islands:
                        continue
                    islands.add(island_name)
                    result += island[island_name]
                board[x][y] = (result % 10)
    for i in board:
        print("".join(map(str, i)))
