import sys

input = sys.stdin.readline

def floyd(n):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    graph[i][j] = 0
                if graph[i][j] <= graph[i][k] + graph[k][j]:
                    continue
                graph[i][j] = graph[i][k] + graph[k][j]

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    graph = [[sys.maxsize] * (N+1) for _ in range(N+1)]
    
    for _ in range(M):
        a, b, cost = map(int, input().split())
        if graph[a][b] > cost:
            graph[a][b] = cost
    floyd(N)
    for i in range(1, N+1):
        for j in range(1, N+1):
            print(graph[i][j] if graph[i][j] != sys.maxsize else 0, end=" ")
        print("")
