import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000001)

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [-1 for i in range(n+1)]

def dfs(num):
    visited[num] = 1

    for elem in graph[num]:
        if visited[elem] == -1:
            visited[elem] = 1
            dfs(elem)


ans = 0
for num in range(1, n+1):
    if visited[num] == -1:
        dfs(num)
        ans += 1
print(ans)