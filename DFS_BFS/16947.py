import sys
from collections import deque

sys.setrecursionlimit(100000)
input = sys.stdin.readline


def find_recursion(parent: int, cur: int):
    # 종료 조건
    # 이미 방문했던 점을 또 방문한다면 이건 순환이 생겼다는 뜻이다.
    if visited[cur] and cur != parent:
        recursion[cur] = True
        # 방문에 시작점을 알려준다.
        return recursion[cur]
    # 방문처리를 한다.
    visited[cur] = True

    flag = True
    # 순환을 찾았는지 확인한다.
    for next in graph[cur]:
        # 방금 방문한 부모는 제외한다.
        if next == parent:
            continue
        result = find_recursion(cur, next)
        if result:
            if recursion[cur]:
                flag = False
            # 순환을 찾았다면 해당 친구는 참으로 만들어준다.
            recursion[cur] = True
    # 순환을 찾았는지 알려준다.
    return recursion[cur] and flag


def solution(n: int, graph: list[list[int]]):
    # 순환선 찾기
    find_recursion(0, 0)

    dist = [0] * n
    # 순환선으로부터 각 역까지의 최소 거리를 구한다.
    dq = deque([])
    for i in range(n):
        # 순환인 곳만 넣는다.
        if recursion[i]:
            dq.append(i)
    while dq:
        cur = dq.popleft()
        for next in graph[cur]:
            # 순환인 곳은 넘어간다.
            if recursion[next]:
                continue
            dist[next] = dist[cur] + 1
            recursion[next] = True
            dq.append(next)
    return dist


if __name__ == "__main__":
    N = int(input())
    visited = [False] * N
    recursion = [False] * N
    graph = [[] for _ in range(N)]
    for _ in range(N):
        x, y = map(int, input().split())
        graph[x-1].append(y-1)
        graph[y-1].append(x-1)
    print(*solution(N, graph))
