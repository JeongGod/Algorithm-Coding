'''
시간 복잡도 기존으로하면 O(n^2) => 4억으로 시간초과
그래서 heap을 사용하여 O(nlogn)로 풀이
'''
import sys, heapq, math
input = sys.stdin.readline

v_num, e = map(int, input().split())
start = int(input())

length = [math.inf for _ in range(v_num+1)]
graph = [[] for _ in range(v_num+1)]

def Dijkstra(start):
    length[start] = 0
    hq = []
    heapq.heappush(hq, (0, start))
    # 모든 간선을 다 확인한다.
    while hq:
        # v노드를 향해 가는 것을 뽑는다.
        total_w, v = heapq.heappop(hq)
        
        # v노드까지 가는길로 저장한 최솟값이 지금 뽑은 weight보다 크다면 볼 필요가 없다.
        if length[v] < total_w:
            continue

        # v노드에서 시작하는 w,v를 확인한다.
        for w,new_v in graph[v]:
            new_total = total_w + w
            # 만약 v노드까지의 최솟값 + (v -> new_v까지 weight) vs 현재 저장되어있는 최솟값
            if length[new_v] > new_total:
                length[new_v] = new_total
                heapq.heappush(hq, (new_total, new_v))

# u- > v, w
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((w,v))

Dijkstra(start)

for ans in length[1:]:
    print(ans if ans != math.inf else "INF")


