import sys
from collections import deque

input = sys.stdin.readline

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def outside(board, edges):
    visited = [[0] * (M - 1) for _ in range(N - 1)]
    dq = deque(edges)

    points = set(edges)
    while dq:
        cx, cy = dq.popleft()

        for dir in dirs:
            nx, ny = cx + dir[0], cy + dir[1]
            if 1 <= nx < N - 1 and 1 <= ny < M - 1 and not visited[nx][ny] and board[nx][ny] != 1:
                visited[nx][ny] = 1
                points.add((nx, ny))
                dq.append((nx, ny))
    
    return points

def check(cheese_points, outside_points):
    points = []
    for cp in cheese_points:
        exposure = 0
        for dir in dirs:
            nx, ny = cp[0] + dir[0], cp[1] + dir[1]
            if (nx, ny) in outside_points:
                exposure += 1
        if exposure >= 2:
            points.append(cp)
    return points

def delete(board, points, cheese_points):
    for x, y in points:
        board[x][y] = 0
        cheese_points.remove((x, y))

if __name__ == "__main__":
    # 2면이 맞닿으면 녹는다.
    # 하지만 내부로 감싸져있으면 녹지 않는다. ->
    # 가장자리는 치즈가 놓이지 않는다.

    # 1. 가장자리 BFS 돌려서 외부 공간 확인
    # 2. 치즈공간 외부 접촉 확인
    # 3. 외부접촉 2 이상 삭제
    # 4. 1번부터 다시 확인

    N, M = map(int, input().split())
    BOARD = [[*map(int, input().split())] for _ in range(N)]
    EDGES = []
    EDGES += [(i, 0) for i in range(N)]
    EDGES += [(N-1, i) for i in range(N)]
    EDGES += [(0, j) for j in range(M)]
    EDGES += [(j, M-1) for j in range(M)]
    
    cheese_points = set()
    for i in range(N):
        for j in range(M):
            if BOARD[i][j] == 1:
                cheese_points.add((i, j))

    answer = 0
    while True:
        outside_points = outside(BOARD, EDGES)
        delete_cheese_points = check(cheese_points, outside_points)

        if len(delete_cheese_points) == 0:
            break
        
        delete(BOARD, delete_cheese_points, cheese_points)
        
        answer += 1
    
    print(answer)