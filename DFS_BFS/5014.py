import sys
from collections import deque
input = sys.stdin.readline

top, cur, target, up, down = map(int, input().split())

dq = deque([(cur, 0)])

visited = [-1 for _ in range(top+1)]
visited[cur] = 1

def check(level):
    if 1 <= level <= top and visited[level] == -1:
        return True
    return False

while dq:
    cur, ans = dq.popleft()

    if cur == target:
        print(ans)
        exit()

    if check(cur+up):
        dq.append((cur+up, ans+1))
        visited[cur+up] = 1
    if check(cur-down):
        dq.append((cur-down, ans+1))
        visited[cur-down] = 1

print("use the stairs")