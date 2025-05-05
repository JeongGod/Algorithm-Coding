import sys
from collections import deque

input = sys.stdin.readline

EMPTY = 0
WALL = 1
VIRUS = 2

def possible_spread(x, y, board):
    if board[x][y] == EMPTY:
        return True
    return False

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def spread(board):
    dq = deque(VIRUS_POINTS)
    
    while dq:
        x, y = dq.popleft()

        for d in dir:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < N and 0 <= ny < M and possible_spread(nx, ny, board):
                board[nx][ny] = VIRUS
                dq.append((nx, ny))
    return board

def check(board):
    safety = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == EMPTY:
                safety += 1
    return safety

ANSWER = 0

def wall(walls):
    copy_board = []
    for i in range(N):
        copy_board.append([*BOARD[i]])
    
    for wx, wy in walls:
        copy_board[wx][wy] = WALL

    return copy_board

def dfs(start_idx, walls):
    global ANSWER
    if len(walls) == 3:
        board = spread(wall(walls))
        ANSWER = max(ANSWER, check(board))
        return

    for idx in range(start_idx, len(EMPTY_POINTS)):
        dfs(idx + 1, walls + [EMPTY_POINTS[idx]])
            

if __name__ == "__main__":
    N, M = map(int, input().split())
    BOARD = []
    VIRUS_POINTS = []
    EMPTY_POINTS = []
    for i in range(N):
        line = [*map(int, input().split())]
        for j in range(M):
            if line[j] == VIRUS:
                VIRUS_POINTS.append((i, j))
            elif line[j] == EMPTY:
                EMPTY_POINTS.append((i, j))
        BOARD.append(line)

    dfs(0, [])
    
    print(ANSWER)