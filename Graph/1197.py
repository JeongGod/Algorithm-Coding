import sys

input = sys.stdin.readline

def find(x : int) -> int:
    if tree[x] == x:
        return x
    tree[x] = find(tree[x])
    return tree[x]

def connect(x : int, y : int) -> None:
    if x < y:
        tree[x] = y
    else:
        tree[y] = x

if __name__ == "__main__":
    answer = 0
    V, E = map(int, input().split())

    tree = [i for i in range(V+1)]
    edges = []
    for _ in range(E):
        a, b, cost = map(int, input().split())
        edges.append((a, b, cost))
    edges.sort(key = lambda x:x[2])

    for x, y, cost in edges:
        px, py = find(x), find(y)
        if px == py:
            continue
        answer += cost
        connect(px, py)
    print(answer)
