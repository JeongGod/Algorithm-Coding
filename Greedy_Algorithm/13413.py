import sys

input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    N = int(input())
    start = list(input().rstrip())
    target = list(input().rstrip())
    b, w = 0, 0
    for i in range(len(start)):
        if start[i] != target[i]:
            if start[i] == "B":
                b += 1
            else:
                w += 1
    print(min(b, w) + abs(b-w))
