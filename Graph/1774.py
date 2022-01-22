import math
import sys

input = sys.stdin.readline

def find(x : int) -> int:
    if tree[x] == x:
        return x
    tree[x] = find(tree[x])
    return tree[x]

def union(x : int, y : int) -> None:
    if x < y:
        tree[x] = tree[y]
    else:
        tree[y] = tree[x]

def solution():
    global tree
    N, E = map(int, input().split())
    tree = [i for i in range(N+1)]
    nodes = []
    edges = []
    for _ in range(N):
        nodes.append(tuple(map(int, input().split())))
    for i in range(N):
        for j in range(i+1, N):
            cost = math.sqrt((nodes[i][0] - nodes[j][0])**2 + (nodes[i][1] - nodes[j][1])**2)
            edges.append((i+1, j+1, cost))

    edges.sort(key=lambda x: x[2])
    for _ in range(E):
        x, y = map(int, input().split())
        union(find(x), find(y))

    answer = 0
    for x, y, cost in edges:
        px, py = find(x), find(y)
        if px == py:
            continue
        answer += cost
        union(px, py)
    
    return answer

if __name__ == "__main__":
    print(f"{solution():.2f}")
