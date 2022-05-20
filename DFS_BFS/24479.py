import sys

sys.setrecursionlimit(100001)
input = sys.stdin.readline

def dfs(cur):
    global visited, cnt
    for ncur in graph[cur]:
        if visited[ncur]:
            continue
        cnt += 1
        visited[ncur] = cnt
        dfs(ncur)


if __name__ == "__main__":
    N, M, R = map(int, input().split())
    visited = [0] * (N+1)
    cnt = 1
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(N+1):
        graph[i].sort()
    
    visited[R] = 1
    dfs(R)
    
    for i in visited[1:]:
        print(i)
