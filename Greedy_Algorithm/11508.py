import sys

input = sys.stdin.readline

N = int(input())
_li = sorted([int(input()) for _ in range(N)], reverse=True)
ans = 0
for i in range(0, N, 3):
    ans += sum(_li[i:i+2])
print(ans)
    
