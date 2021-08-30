import sys

input = sys.stdin.readline

while True:
    N, *rest = map(int, input().split())
    visited = [0 for _ in range(N)]
    if N == 0:
        break

    ans = 0
    def dfs(depth, result):
        global ans
        if depth == 6:
            print(*result[1:])
            return
        for idx, num in enumerate(rest):
            if not visited[idx] and result[-1] <= num:
                visited[idx] = 1
                dfs(depth+1, result+[num])
                visited[idx] = 0
    dfs(0, [-1])
    print("")
