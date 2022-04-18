import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    pdict = defaultdict(list)
    cnt_problem = defaultdict(int)
    associate = set()
    for _ in range(M):
        x, y = map(int, input().split())
        pdict[x].append(y)
        cnt_problem[y] += 1
        associate.add(y)

    hq = []
    answer = []
    for i in range(1, N+1):
        if not i in associate:
            heapq.heappush(hq, i)

    while hq:
        x = heapq.heappop(hq)
        answer.append(x)
        
        result = pdict.get(x)
        if result is not None:
            for next in result:
                cnt_problem[next] -= 1
                if cnt_problem[next] != 0:
                    continue
                heapq.heappush(hq, next)
        
    print(*answer)
    
"""
7 6
6 7
5 6
3 5
2 7
4 2
5 4
"""
