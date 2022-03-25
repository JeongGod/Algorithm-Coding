import sys

input = sys.stdin.readline


def dfs(cur: int, cnt: int) -> bool:
    if cnt == 5:
        return True

    for next in friends[cur]:
        if visited[next]:
            continue
        visited[next] = True

        result = dfs(next, cnt+1)
        if result:
            return True
        visited[next] = False
    return False


def solution(n: int, friends: list[list[int, int]]) -> int:
    # dfs로 탐색해서 5이상 넘어가면 true
    for start in range(n):
        visited[start] = True
        if dfs(start, 1):
            return 1
        visited[start] = False
    return 0


if __name__ == "__main__":
    N, M = map(int, input().split())
    friends = [[] for _ in range(N)]
    visited = [False] * N
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a].append(b)
        friends[b].append(a)

    print(solution(N, friends))
