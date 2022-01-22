import heapq
import sys

input = sys.stdin.readline

def dijstra(n : int) -> int:
    """
    1. 시작지점 하나를 정합니다.
    2. 연결되어있는 지점에서 가장 작은 가중치를 가진 곳을 방문합니다.
    3. 방문처리 후, 2번을 반복합니다.
    """
    answer = 0
    hq = [(0, 1)]
    visited = [False] * (n+1)
    while hq:
        cost, cur = heapq.heappop(hq)
        if visited[cur]:
            continue
        visited[cur] = True
        answer += cost
        for next_v, next_cost in graph[cur]:
            if visited[next_v]:
                continue
            heapq.heappush(hq, (next_cost, next_v))
    return answer

if __name__ == "__main__":
    answer = 0
    V = int(input())
    E = int(input())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b, cost = map(int, input().split())
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    
    
    print(dijstra(n=V))
