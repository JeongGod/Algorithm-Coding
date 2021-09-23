import sys

input = sys.stdin.readline

N = int(input())
_li = sorted(list(map(int, input().split())))

ans, tmp = 0, 0
for i in _li:
    tmp = tmp + i
    ans += tmp
print(ans)
