import sys
import heapq
input = sys.stdin.readline
"""
Greedy하게 진행해야한다.
먼저 작은 것 2개를 합친다.
1. 합친 것의 값 > 다른 두 개의 페이지의 값
    두 개를 합친다.
2. 합친 것의 값 < 다른 두 개의 페이지의 값
    1. 합친 것 + 두 개중 작은 값
"""
T = int(input())
for _ in range(T):
    N = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files)
    answer = 0
    while len(files) > 1:
        a, b = heapq.heappop(files), heapq.heappop(files)
        answer += (a+b)
        heapq.heappush(files, a+b)
    print(answer)
           