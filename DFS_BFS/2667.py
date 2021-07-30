import sys
from collections import deque
input = sys.stdin.readline

house = []
n = int(input())
for i in range(n):
    house.append(list(input().rstrip()))

dir = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(i,j):
    dq = deque([(i,j)])
    cnt = 0
    while dq:
        x, y = dq.popleft()
        cnt += 1
        for idx in dir:
            nx, ny = x+idx[0], y+idx[1]
            if 0 <= nx < n and 0 <= ny < n and house[nx][ny] == "1":
                dq.append((nx,ny))
                house[nx][ny] = "0"
    return cnt
result = []
for i in range(n):
    for j in range(n):
        if house[i][j] == "1":
            house[i][j] = "0"
            result.append(bfs(i, j))
print(len(result))
print(*sorted(result), sep="\n")