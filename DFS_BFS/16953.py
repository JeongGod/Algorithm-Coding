'''
a -> b로 간다는 생각으로 bfs로 풀었다. dfs로도 풀 수 있겠지만 결국 a -> b로 가는 생각에 사로잡혀있었다.
하지만 b -> a로 가게 한다면 더 빠르게 갈 수 있다..
'''
import sys
from collections import deque
input = sys.stdin.readline

n, target = map(int, input().split())

def bfs(n):
    dq = deque([(n,1)])
    while dq:
        x,ans = dq.popleft()
        
        nx1, nx2 = int(str(x)+"1") , x*2
        if nx1 == target or nx2 == target:
            return ans+1
        if nx1 < target:
            dq.append((nx1, ans+1))
        if nx2 < target:
            dq.append((nx2, ans+1))
result = bfs(n)
print(result if result != None else -1)