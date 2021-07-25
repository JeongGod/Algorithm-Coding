# 다익스트라 (Dijkstra) 알고리즘
- `시작 정점`이 주어지면 그래프에서 `모든 정점`에 대한 `최단거리`를 구할 수 있는 알고리즘이다.

알아둘 점
1. 음수의 간선이 주어지면 최단거리를 구하지 못한다.
2. 다이나믹 프로그래밍(DP)를 이용한다.

시간복잡도
- O(n^2)
- O(ElogE) => O(ElogV)
    => 해당 이유는 밑에서 서술

먼저 시간복잡도가 O(n^2)인 경우를 보자.
1. 시작 노드를 정한다.
2. 시작 노드에서 이어진 노드들의 간선 중 가장 작은 간선을 가진 노드를 방문한다.
3. 해당 노드에서 이어진 간선 + 시작 노드까지의 최솟값 , 해당 노드까지의 최솟값을 비교한다.
4. 2~3번을 반복한다.

```python
import math
visited = set()
dp = [math.inf for _ in range(n)]
dp[start] = 0
while True:
    # 최단거리 찾기
    val = math.inf
    cur = 0
    for vertex in range(len(dp)):
        if dp[vertex] < val and not vertex in visited:
            val = dp[vertex]
            cur = vertex
    
    # 최단거리를 찾지 못했다면 나온다.
    if val == math.inf:
        break
    # 최단거리를 찾았다면
    for w,v in graph[cur]:
        weight = w + dp[cur]
        if weight < dp[v] and not v in visited:
            dp[v] = weight
```

시간복잡도 O(ElogN)인 경우이다.
아까 O(ElogE)도 되는 이유는 확실히 하자면 O(ElogE)가 맞는 표기이다. 하지만 간선의 개수가 최대 V^2의 경우이므로 O(ElogN)으로도 표현 가능하다.

- 위 내용과 다를게 없다. 최소힙만 잘 사용하면 이렇게도 구현이 가능하다.
```python
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
```
