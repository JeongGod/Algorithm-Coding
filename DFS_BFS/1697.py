import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

visited = [0] * 200001
dq = deque([(N, 0)])
visited[N] = 1
while dq:
    cur, t = dq.popleft()
    if cur == K:
        print(t)
        break

    for next_pos in [cur+1, cur-1, cur*2]:
        if 0 <= next_pos < len(visited) and visited[next_pos] == 0:
            visited[next_pos] = 1
            dq.append((next_pos, t+1))
