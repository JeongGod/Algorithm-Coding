import heapq
import sys
from typing import List, Tuple

input = sys.stdin.readline

def solution(conference : List[Tuple[int, int]]):
    hq = []
    answer = 0

    for start, end in conference:
        
        # 가능한 회의실 빼기
        while hq:
            if hq[0] > start:
                break
            heapq.heappop(hq)
        
        heapq.heappush(hq, end)
        answer = max(answer, len(hq))

    return answer


if __name__ == "__main__":
    N = int(input())
    _list = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x:x[0])
    print(solution(conference=_list))
