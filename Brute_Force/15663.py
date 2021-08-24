import sys
from collections import Counter

input = sys.stdin.readline

N, M = map(int, input().split())
li = sorted(list(map(int, input().split())))

visited = [0] * N
dup = set()

def dfs(ans):
    if len(ans) == M:
        if not tuple(ans) in dup:
            print(*ans)
            dup.add(tuple(ans))
            return
    for idx in range(len(li)):
        if not visited[idx]:
            visited[idx] = 1
            dfs(ans + [li[idx]])
            visited[idx] = 0
dfs([])