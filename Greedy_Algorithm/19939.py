import sys

input = sys.stdin.readline

N, K = map(int, input().split())

total = ((1+K)*K) // 2
if N < total:
    print(-1)
    exit()

if (N - total)%K == 0:
    print(K-1)
else:
    print(K)
