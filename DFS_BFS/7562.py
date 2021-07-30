import sys
from collections import deque
input = sys.stdin.readline


tc = int(input())

dir = [(-2,1), (-2,-1), (-1,2), (-1,-2), (1,2), (1,-2), (2,1), (2,-1)]

for _ in range(tc):
    n = int(input())
    cur_x, cur_y = map(int, input().split())
    tar_x, tar_y = map(int, input().split())
    visited = [[-1]*n for i in range(n)]
    dq = deque([(cur_x, cur_y, 0)])
    while dq:
        x, y, num = dq.popleft()
        if x == tar_x and y == tar_y:
            break
        for idx in dir:
            nx, ny = x+idx[0], y+idx[1]
            if 0<= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                visited[nx][ny] = 1
                dq.append((nx, ny, num+1))
    print(num)