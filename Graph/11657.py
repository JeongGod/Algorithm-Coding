import sys
from typing import List, Tuple

input = sys.stdin.readline

MAX_DIST = sys.maxsize

def bellman_ford(n : int, edges : List[Tuple], dist : List) -> bool:
    """
    """
    for _ in range(n-1):
        for s, d, cost in edges:
            # 한 번도 방문하지 않은 노드인 경우
            if dist[s] == MAX_DIST:
                continue
            # 이미 최단거리인 경우
            if dist[s] + cost >= dist[d]:
                continue
            dist[d] = dist[s] + cost

    for s, d, cost in edges:
        if dist[s] == MAX_DIST or dist[s] + cost >= dist[d]:
            continue
        return False
    return True


if __name__ == "__main__":
    N, M = map(int, input().split())
    edges = []
    dist = [MAX_DIST] * (N+1)
    dist[1] = 0

    for _ in range(M):
        s, d, cost = map(int, input().split())
        edges.append((s, d, cost))
    
    if not bellman_ford(n=N, edges=edges, dist=dist):
        print(-1)
    else:
        for i in range(2, N+1):
            print(dist[i] if dist[i] != MAX_DIST else -1)
    
