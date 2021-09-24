import sys

input = sys.stdin.readline

N = int(input())
confer = sorted([tuple(map(int, input().split())) for _ in range(N)])

start, end = -1, -1
ans = 0
for n_start, n_end in confer:
    # 더 줄일 수 있는지 판단
    if end > n_start:
        end = min(end, n_end)

    # 회의실 하나 추가
    else:
        start, end = n_start, n_end
        ans += 1
print(ans)
