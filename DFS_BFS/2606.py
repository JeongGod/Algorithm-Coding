import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

_list = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    _list[x].append(y)
    _list[y].append(x)

visited = [-1 for _ in range(n+1)]
visited[1] = 1
li = [1]
ans = 0
while li:
    com = li.pop()
    for num in _list[com]:
        if visited[num] == -1:
            ans += 1
            li.append(num)
            visited[num] = 1

print(ans)