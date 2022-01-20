import sys

input = sys.stdin.readline

"""
1. 음수의 사이클을 확인하면 된다.
2. 보통의 벨만포드는 방문한 노드의 간선을 확인하여 갱신시키는 방법으로 진행했다.(INF로 놓아 연결이 되어있지 않다고 생각)
3. 그렇게 하면 1번 노드에서 시작을 한다고 가정했을 시, 아무도 1번 노드와 연결되지 않았다면 제대로 탐색이 불가능하다.
4. 모든 노드를 시작 노드로 잡고 벨만포드를 돌리면 O(N*NM)으로 시간초과가 난다.
<해결 방법>
1. 가상의 노드를 만들어 모든 노드와 0의 가중치로 연결되어있다고 생각하는 방법
2. 모든 노드가 시작 노드로 동시에 시작한다고 생각하고 푼다.
"""

def bellman_ford(n : int, dist : list, edges : tuple) -> bool:
    for i in range(1, n+1):
        for s, e, cost in edges:
            if dist[s] + cost >= dist[e]:
                continue
            if i == n:
                return True
            dist[e] = dist[s] + cost
    return False



if __name__ == "__main__":
    TC = int(input())

    for _ in range(TC):
        N, M, W = map(int, input().split())
        dist = [0] * (N+1)
        edges = []
        for _ in range(M):
            s, e, cost = map(int, input().split())
            edges.append((s, e, cost))
            edges.append((e, s, cost))
        
        for _ in range(W):
            s, e, cost = map(int, input().split())
            edges.append((s, e, -cost))
        
        if bellman_ford(n=N, dist=dist, edges=edges):
            print("YES")
        else:
            print("NO")
