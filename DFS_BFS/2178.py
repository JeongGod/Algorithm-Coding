'''
전형적인 미로탐색. bfs로 최단경로 구하자.
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
maze = []
dq = deque([(0,0,0)])

for i in range(n):
    maze.append(list(input().rstrip()))

dir = [(0,1), (0,-1), (1,0), (-1,0)]
def bfs():
    while dq:
        x, y, ans = dq.popleft()
        if x == n-1 and y == m-1:
            return ans+1
        
        for idx in dir:
            nx, ny = x+idx[0], y+idx[1]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == "1":
                dq.append((nx, ny, ans+1))
                maze[nx][ny] = "0"

print(bfs())