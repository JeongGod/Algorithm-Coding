import sys

input = sys.stdin.readline

def make_one(x, y):
    if rank[x] < rank[y]:
        rank[x] = rank[y]
        tree[x] = y
    elif rank[x] > rank[y]:
        rank[y] = rank[x]
        tree[y] = x
    else:
        rank[x] += 1
        rank[y] += 1
        tree[y] = x

def search(n : int):
    # 자기 자신이 부모라면
    if tree[n] == n:
        return n
    tree[n] = search(tree[n])
    return tree[n]

if __name__ == "__main__":
    N, M = map(int, input().split())
    tree = [i for i in range(N)]
    rank = [1] * N
    for i in range(M):
        x, y = map(int, input().split())
        px, py = search(n=x), search(n=y)
        # 부모가 같으면 넘긴다.
        if px == py:
            print(i+1)
            exit(0)
        # 부모를 연결한다.
        make_one(px, py)
    print(0)
