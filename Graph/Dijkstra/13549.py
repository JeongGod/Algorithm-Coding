'''
        걷는다면 1초후에 X-1 or X+1
        순간이동 0초후에 2*X

        수빈이가 동생을 찾을 수 있는 가장 빠른 시간

        5 -> 4, 3 -> 10
        dp[i] = min(dp[i//2], dp[i-1]+1, dp[i+1]-1)
'''
import sys
from collections import deque
input = sys.stdin.readline

visited = [1e9] * 100001

start, dest = map(int, input().split())
dq = deque([start])
visited[start] = 0
def calc(x):
    return [(x*2,0), (x-1,1), (x+1,1)]

while dq:
    cur = dq.popleft()
    
    next = calc(cur)
    for elem, cost in next:
        if 0<= elem <= 100000 and visited[elem] == 1e9:
            visited[elem] = min(visited[cur] + cost, visited[elem])
            dq.append(elem)
print(visited[dest])
