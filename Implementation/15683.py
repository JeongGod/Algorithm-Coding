import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

# 오른, 왼, 아래, 위
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def spread(cctves, cctv_directions):
    # visited에 방향 설정
    copy_board = [[1] * M for _ in range(N)]
    for (i, j) in WALLS:
        copy_board[i][j] = 0
    visited = [[[False, False, False, False] for _ in range(M)] for _ in range(N)]

    dq = deque()
    for idx, (_, x, y) in enumerate(cctves):
        for dir_idx in cctv_directions[idx]:
            visited[x][y][dir_idx] = True
            copy_board[x][y] = 0
            dq.append((x, y, dir_idx))

    while dq:
        cx, cy, dir_idx = dq.popleft()
        dir = dirs[dir_idx]
        # cctv 방향
        nx, ny = cx + dir[0], cy + dir[1]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny][dir_idx] and BOARD[nx][ny] != 6:
            # 방문
            visited[nx][ny][dir_idx] = True
            # 사각지대
            copy_board[nx][ny] = 0
            dq.append((nx, ny, dir_idx))

    return copy_board

def count(copy_board):
    ans = 0
    for i in range(N):
        ans += sum(copy_board[i])
    return ans

ANSWER = 64
def dfs(idx, cctves, cctv_directions):
    global ANSWER
    if (len(cctv_directions) == len(cctves)):
        ANSWER = min(ANSWER, count(spread(cctves, cctv_directions)))
        return
    cctv = cctves[idx][0]

    match cctv:
        case 1:
            for index in range(4):
                dfs(idx + 1, cctves, cctv_directions + [[index]])
        case 2:
            dfs(idx + 1, cctves, cctv_directions + [[0, 1]])
            dfs(idx + 1, cctves, cctv_directions + [[2, 3]])
        case 3:
            for com in combinations(range(4), 2):
                # 반대 방향 제외
                if (com[0] == 0 and com[1] == 1) or (com[0] == 2 and com[1] == 3):
                    continue
                dfs(idx + 1, cctves, cctv_directions + [com])
        case 4:
            for com in combinations(range(4), 3):
                dfs(idx + 1, cctves, cctv_directions + [com])
        case 5:
            dfs(idx + 1, cctves, cctv_directions + [[0, 1, 2, 3]])

def solution():
    pass

# 17:15 시작
if __name__ == "__main__":
    # 1. 방향 설정.
    # 2. 방향대로 퍼져나감.
    # 3. 개수 확인
    # 4. 반복
    
    N, M = map(int, input().split())
    BOARD = []
    cctves = []
    WALLS = set()
    for i in range(N):
        line = [*map(int, input().split())]
        for j in range(M):
            if line[j] == 6:
                WALLS.add((i, j))
            elif line[j] != 0:
                cctves.append((line[j], i, j))
        BOARD.append(line)
    
    dfs(0, cctves, [])

    print(ANSWER)