import sys

input = sys.stdin.readline

N, L = map(int, input().split())
H = sorted(list(map(int, input().split())))

for fruit in H:
    if fruit <= L:
        L += 1
        continue
    break
print(L)
