import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N = int(input())
POP = [0] + list(map(int, input().split()))
graph = [[],]
visited = [0] * (N)
a = set()

for _ in range(N):
    _, *wired = map(int, input().split())
    graph.append(list(wired))

ans = sys.maxsize

def bfs(start, check_li):
    tmp_visit = set()
    dq = deque([start])
    tmp_visit.add(start)
    while dq:
        cur = dq.popleft()

        for next in graph[cur]:
            if next not in tmp_visit and next in check_li:
                tmp_visit.add(next)
                dq.append(next)
    
    if len(tmp_visit) == len(check_li):
        return True
    else:
        return False
    

_li = list(range(1, N+1))
# 두 구의 차를 보는것이기 때문에 N//2까지만 보면 된다.
for i in range(1, N//2 +1):
    for com in combinations(_li, i):
        # 연결되어있는 친구라면
        blue = [i for i in range(1,N+1) if i not in com]
        if bfs(com[0], set(com)) and bfs(blue[0], set(blue)) :
            result = abs(sum([POP[i] for i in com]) - sum([POP[i] for i in blue]))
            ans = min(ans, result)

print(ans if ans != sys.maxsize else -1)
