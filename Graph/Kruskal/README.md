# Kruskal 알고리즘
- 최소 비용 신장 트리를 찾는 알고리즘이다.

1. 최소 비용의 간선으로 구성되어야 한다.
2. 사이클을 포함하지 않아야 한다.

위 두 조건을 만족할 때 사용할 수 있다.

여기서 Union-Find 알고리즘과 Prim 알고리즘이 있다.

## Union-Find 알고리즘
---
Disjoin Set(서로 중복되지 않는 부분 집합들)을 표현할 때 사용하는 알고리즘이다.

트리 구조로 변환하여 이용하는 것이 가장 효율적이다.   
그 이유는 밑에 코드를 보면서 알아보자.

```python
# 초기화
for i in range(n+1)
    tree[i] = i
    rank[i] = 1

def find(x):
    if tree[x] == x:
        return x
    tree[x] = find(tree[x])
    return tree[x]

def union(x, y):
    rx = find(x)
    ry = find(y)

    if rx == ry:
        continue
    
    if rank[rx] < rank[ry]:
        tree[rx] = ry
    else:
        tree[ry] = rx
        if rank[rx] == rank[ry]:
            rank[ry] += 1
```
- Find()
    - 위 함수는 재귀적으로 부모노드를 찾는 것으로 생각하면 된다.
    - 여기서 `tree[x] = find(tree[x])` 를 넣은 이유는 최악일 경우는 tree에 꼬리의 꼬리를 물고 리스트의 형태를 띄웠을 경우이다.
    해당 경우에는 한 번만 최악인 O(n)으로 돌게 하고, 다음에는 제일 부모노드를 바라보게끔 하여 추후에 find를 하면 O(1)로 탐색가능하게 한다.

- Union(x,y)
    - 위 함수는 find함수의 영향을 많이 받는다.
    - 그래서 union을 할 경우 추후에 find를 할 때 도움을 주기 위해서 rank라는 것을 도입한다.
    - rank란 트리의 깊이를 뜻한다. 트리의 깊이에 연연하지 않고 마구잡이로 붙이면 트리가 엄청 깊어져 비효율적으로 find를 할 수 있다.
    - 이를 방지하기 위해서 트리를 얕은 쪽 => 깊은 쪽으로 붙여 트리의 높이가 일정하도록 만들어 주어 find시 효율적으로 만들어준다.

## Prim 알고리즘

현재 묶여있는 정점중에서 가장 작은 간선을 택해서 잇는 방법이다.

1. O(n^2)
```python
import math

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
for i in range(m):
    x,y,w = map(int, input().split())
    graph[x].append((w,y))
    graph[y].append((w,x))

visited = set()
dp = [math.inf for _ in range(n+1)]
dp[1] = 0
ans = 0
while True:
    # 최단거리 찾기
    val = math.inf
    cur = 0
    for vertex in range(len(dp)):
        if dp[vertex] < val and not vertex in visited:
            val = dp[vertex]
            cur = vertex
    visited.add(cur)
    print(dp)
    # 최단거리를 찾지 못했다면 나온다.
    if val == math.inf:
        break
    # 최단거리를 찾았다면
    for w,v in graph[cur]:
        if not v in visited:
            dp[v] = min(dp[v], w)
    ans += val
```

2. O(ElogE)
내일 업데이트 예정