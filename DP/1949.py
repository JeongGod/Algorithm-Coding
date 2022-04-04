import sys

input = sys.stdin.readline

sys.setrecursionlimit(100000)

def dfs(graph : list[list[int]], town_people : list[int], cur : int) -> None:
    global visited, dp
    dp[cur][0] = town_people[cur]
    dp[cur][1] = 0
    for ncur in graph[cur]:
        # 방문했던 점이라면
        if visited[ncur]:
            continue
        visited[ncur] = True
        # 계속해서 트리의 끝을 향해 내려간다.
        dfs(graph, town_people, ncur)
        # cur이 우수 마을일 경우
        dp[cur][0] += dp[ncur][1]
        # cur이 우수 마을이 아닐 경우
        dp[cur][1] += max(dp[ncur][1], dp[ncur][0])



def solution(town_people : list[int], graph : list[list[int]]) -> int:
    global visited, dp
    """
    내가 이겼다면 True
    내가 지고 자식들이 이겼다면 False
    """
    visited = [False] * len(town_people)
    dp = [[0, 0] for _ in range(len(town_people))]
    visited[0] = True
    dfs(graph, town_people, 0)
    return max(dp[0])
    

if __name__ == "__main__":
    N = int(input())
    town_people = list(map(int, input().split()))
    graph =[[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    print(solution(town_people, graph))
