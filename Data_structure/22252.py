import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline

def solution() -> int:
    N = int(input())
    trade = defaultdict(list)
    answer = 0
    for _ in range(N):
        cmd, person, *rest = list(input().split())
        if cmd == "1":
            for i in map(int, rest[1:]):
                heapq.heappush(trade[person], -i)
        else:
            pop_cnt = int(rest[0])
            for _ in range(pop_cnt):
                if not trade[person]:
                    break
                answer += -heapq.heappop(trade[person])
    return answer
if __name__ == "__main__":
    print(solution())
