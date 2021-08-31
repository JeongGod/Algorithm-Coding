import sys

sys.setrecursionlimit(2000000)

input = sys.stdin.readline

N = int(input())
chu = list(map(int, input().split()))
visited = [0] * 2600005

ans = 0
def dfs(depth, weight):
    global ans
    if depth == N:
        if weight > 0 and not visited[weight]:
            visited[weight] = 1
            ans += 1
        return

    dfs(depth+1, weight)
    dfs(depth+1, weight+chu[depth])
    dfs(depth+1, weight-chu[depth])

dfs(0, 0)
print(sum(chu)-ans)

'''
한 번만 이용 양팔 저울
처음에 아무것도 추를 넣지 않은 상태로 진행
추를 하나 넣고 진행
추를 두개 넣고 진행...
추를 넣었을 때 나머지

memoization을 활용하면 되겠다.
'''
