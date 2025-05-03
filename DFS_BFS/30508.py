from collections import deque
from re import L
import sys

input = sys.stdin.readline


def water():
    dq = deque(HOLES)
    visited = [[1] * (M+1) for _ in range(N+1)]
    dir = [(0,1), (0,-1), (1,0), (-1,0)]
    while dq:
        x, y, height = dq.popleft()
        visited[x][y] = 0

        for idx in dir:
            nx, ny = x+idx[0], y+idx[1]
            if 1 <= nx <= N and 1 <= ny <= M and visited[nx][ny] == 1:
                if MAP[nx-1][ny-1] < height:
                    continue
                dq.append((nx, ny, MAP[nx-1][ny-1]))
                visited[nx][ny] = 0

    return visited

if __name__ == "__main__":
    # K개의 칸에는 하수구
    # 인접한 높이가 자신보다 낮거나, 같은 칸에 하수구나 물이 빠진 칸이 있으면 물이 빠진다.
    # 하수구가 없는 칸 중 물이 빠지지 않은 칸을 물이 고인 칸
    # 물이 고인 칸을 디디지 않고 간다.
    N, M = map(int, input().split())
    H, W = map(int, input().split())
    MAP = []
    for _ in range(N):
        MAP.append([*map(int, input().split())])
    K = int(input())

    HOLES = []
    for _ in range(K):
        x, y = map(int, input().split())
        HOLES.append((x , y, MAP[x-1][y-1]))

    sum_map = water()

    sum_map[0][1] = sum_map[0][0] + sum_map[0][1]
    sum_map[1][0] = sum_map[0][0] + sum_map[1][0]
    for i in range(1, N+1):
        for j in range(1, M+1):
            sum_map[i][j] = sum_map[i-1][j] + sum_map[i][j-1] - sum_map[i-1][j-1] + sum_map[i][j]
    ans = 0
    for i in range(1, N-H+2):
        for j in range(1, M-W+2):
            if (sum_map[i+H-1][j+W-1] - sum_map[i+H-1][j-1] - sum_map[i-1][j+W-1] + sum_map[i-1][j-1] == 0):
                ans += 1
    
    print(ans)




# 2  6X 7X 8X 8X
# 2  3X 3X 7X 9X
# 4  5X 2  6X 5X
# 3  2  1  3  4X
# 5  7  9  8X 1X