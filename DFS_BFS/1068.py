import sys

input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]

root = []
for idx, val in enumerate(map(int, input().split())):
    if val == -1:
        root.append(idx)
    else:
        tree[val].append(idx)
M = int(input())

tree[M] = [-1]
ans = 0
"""
1. 루트노드는 리프노드로 취급하지 않는다.
2. 자식노드가 1개인데 삭제가 되었다면 그러면 부모노드가 리프노드가 된다.
"""


def dfs(cur, rank):
    global ans
    # 삭제된 노드는 리프노드취급하지 않는다.
    if tree[cur] == [-1]:
        return
    if tree[cur] == []:
        ans += 1
        return

    for i in tree[cur]:
        # 현재 나의 자식은 1명이고 그 자식이 삭제된 녀석인지 체크
        if len(tree[cur]) == 1 and tree[i] == [-1]:
            ans += 1
            return
        dfs(i, rank+1)


for i in root:
    # 루트노드는 리프노드로 취급하지 않는다.
    if tree[i] == [] or tree[i] == [-1]:
        continue
    dfs(i, 1)
print(ans)
