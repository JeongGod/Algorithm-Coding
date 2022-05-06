import sys
from collections import defaultdict
from heapq import heappop, heappush

input = sys.stdin.readline


def top_val(hq, cnt, sign):
    while hq:
        if sign:
            val = -hq[0]
        else:
            val = hq[0]
        
        if cnt[val] != 0:
            return val
        
        if cnt[val] == 0:
            heappop(hq)
            continue

    return -1

def solution():
    N = int(input())
    max_hq = []
    min_hq = []
    cnt = defaultdict(int)
    for _ in range(N):
        com, val = input().rstrip().split()
        if com == 'I':
            val = int(val)
            heappush(max_hq, -val)
            heappush(min_hq, val)
            cnt[val] += 1
        elif com == 'D':
            if val == '-1':
                top_val(min_hq, cnt, False)
                if min_hq:
                    cnt[heappop(min_hq)] -= 1
                
            else:
                top_val(max_hq, cnt, True)
                if max_hq:
                    cnt[-heappop(max_hq)] -= 1
    
    # 출력
    
    x = top_val(max_hq, cnt, True)
    y = top_val(min_hq, cnt, False)
    if not max_hq or not min_hq:
        return "EMPTY"
    return x, y

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        result = solution()
        if result != "EMPTY":
            print(*result)
        else:
            print(result)
