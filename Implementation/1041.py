import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline


dir = {
    "A": {"B", "C", "D", "E"},
    "B": {"A", "C", "D", "F"},
    "C": {"A", "B", "F", "E"},
    "D": {"A", "B", "F", "E"},
    "E": {"A", "C", "D", "F"},
    "F": {"B", "C", "D", "E"}
}

def find_min_value(start, count):
    ans = 50 * 3
    for comb in combinations(dir[start], count):
        # combination에서 뽑은 값이 반대편에 속하는 값이면 안된다.
        if len(comb) == 2:
            ax, ay = comb
            if not ax in dir[ay] or not ay in dir[ax]:
                continue
        ans = min(sum(map(lambda x: DICE[x], comb)) + DICE[start], ans)

    return ans


    

if __name__ == "__main__":
    N = int(input())
    DICE_VALUE = [*map(int, input().split())]
    
    DICE = {
        "A": DICE_VALUE[0],
        "B": DICE_VALUE[1],
        "C": DICE_VALUE[2],
        "D": DICE_VALUE[3],
        "E": DICE_VALUE[4],
        "F": DICE_VALUE[5]
    }
    
    if (N == 1):
        print(sum(DICE_VALUE) - max(DICE_VALUE))
    else:
        # 각 연결되어있는 것 끼리 가장 작은 수를 구한다.
        # 1개의 면, 2개의 면, 3개의 면
        one_min_value = min(DICE_VALUE)
        two_min_value = 50*3
        three_min_value = 50*3
        for start in dir.keys():
            two_min_value = min(two_min_value, find_min_value(start, 1))
            three_min_value = min(three_min_value, find_min_value(start, 2))
        print(three_min_value * 4 + two_min_value * (8*N - 12) + one_min_value * (4*N*N - 4*N - (8*N - 12) - 4 + (N -2)**2))
