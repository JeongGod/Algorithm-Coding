import sys

input = sys.stdin.readline

def find(x):
    if x == root[x]:
        return x
    root[x] = find(root[x])
    return root[x]

def union(a, b):
    if a < b:
        root[a] = b
    else:
        root[b] = a

def kruskal(n : int, edges : list[int, int, int]) -> int:
    global root
    edges.sort(key=lambda x: x[2])
    answer = 0
    last_weight = 0
    root = [i for i in range(n)]
    for a, b, weight in edges:
        ra, rb = find(a-1), find(b-1)
        if ra == rb:
            continue
        last_weight = weight
        answer += weight
        union(ra, rb)

    return answer - last_weight

import heapq


def prim(n : int, graph : list[list[int, int]]):
    hq = [(0, 0)]
    visited = [False] * n
    max_weight = 0
    answer = 0
    while hq:
        weight, cur = heapq.heappop(hq)
        if visited[cur]:
            continue
        answer += weight
        if max_weight < weight:
            max_weight = weight
        visited[cur] = True
        for nv, nw in graph[cur]:
            if visited[nv]:
                continue
            heapq.heappush(hq, (nw, nv))
    return answer - max_weight

if __name__ == "__main__":
    N, M = map(int, input().split())
    # kruskal
    edges = [list(map(int, input().split())) for _ in range(M)]
    print(kruskal(N, edges))

    # prim
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b, weight = map(int, input().split())
        graph[a-1].append((b-1, weight))
        graph[b-1].append((a-1, weight))
    print(prim(N, graph))

