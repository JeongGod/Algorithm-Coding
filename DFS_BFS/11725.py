'''
무조건 1이 루트다.
1을 가지고 있는 친구만 따로 저장. 그 곳이 dfs의 첫번째 친구
나머지는 양쪽방향으로 다 저장한다. 메모리는 20만의 배열을 저장할테니 괜찮다.
'''
import sys
input = sys.stdin.readline

n = int(input())
stack = []
tree = [[] for i in range(n+1)]
ans = [0 for i in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    if a == 1:
        stack.append(b)
        ans[b] = 1
    elif b == 1:
        stack.append(a)
        ans[a] = 1
    else:
        tree[a].append(b)
        tree[b].append(a)
while stack:
    cur = stack.pop()
    while tree[cur]:
        next = tree[cur].pop()
        if ans[next] == 0:
            stack.append(next)
            ans[next] = cur
print(*ans[2:], sep='\n')
# print(ans);