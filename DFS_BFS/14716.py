import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().rstrip().split())

board = [list(map(int, input().rstrip().split())) for _ in range(M)]

dist = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
ans = 0
for x in range(M):
    for y in range(N):
        if board[x][y] == 1:
            ans += 1
            # BFS
            board[x][y] = 0
            dq = deque([(x, y)])
            while dq:
                ax, ay = dq.popleft()
                for gx, gy in dist:
                    nx, ny = ax+gx, ay+gy
                    if 0 <= nx < M and 0 <= ny < N and board[nx][ny] == 1:
                        board[nx][ny] = 0
                        dq.append((nx, ny))
print(ans)

# for i in range(250):
#     a = ""
#     for j in range(250):
#         a += "1 "
#     print(a)
