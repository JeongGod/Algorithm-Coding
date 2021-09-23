import sys

input = sys.stdin.readline

N, A, D = map(int, input().split())
part = list(map(int, input().split()))

ans = 0
for i in part:
    if i == A + (D*ans):
        ans += 1
print(ans)
