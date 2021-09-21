import sys

input = sys.stdin.readline

TC = int(input())
for i in range(TC):
    a, b = input().split()
    cnt = [0, 0]
    for idx in range(len(a)):
        if a[idx] != b[idx]:
            cnt[int(a[idx])] += 1
    print(max(cnt))
