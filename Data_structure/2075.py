import heapq
import sys
n = int(sys.stdin.readline())

hq = []
# 최소 힙 사용
# root는 최댓값중에서 5번째로 작은 값을 찾는 것이다.
# tree의 개수를 n개로 유지하면서 작은 값은 버리고, 큰 값일땐 pop and push하면 작은 값이 나온다.
for _ in range(n):
    li = list(map(int, sys.stdin.readline().split()))
    for i in range(n):
        if len(hq) < n:
            heapq.heappush(hq, li[i])
        else:
            if hq[0] < li[i]:
                heapq.heappop(hq)
                heapq.heappush(hq, li[i])
print(heapq.heappop(hq))