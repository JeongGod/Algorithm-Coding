import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = sorted(list(set(map(int, input().split()))))

def dfs(ans, last):
    if len(ans) == M:
        print(*ans)
        return;
    for num in data:
        if num >= last:
            dfs(ans+[num], num)
dfs([], 0)