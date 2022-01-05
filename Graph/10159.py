import sys

input = sys.stdin.readline

"""
플로이드워샬알고리즘을 이용하여 모든 정점간의 연결을 확인한다.
방향성을 가지고 있어야 한다. 대소비교를 해야하니.
"""
N = int(input())
M = int(input())

graph = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    graph[a][b] = 1
    graph[b][a] = -1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] * graph[k][j] != 1:
                continue
            graph[i][j] = graph[i][k]

for line in graph:
    cnt = -1
    for num in line:
        if num == 0:
            cnt += 1
    print(cnt)