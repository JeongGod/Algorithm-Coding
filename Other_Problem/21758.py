import sys
from typing import List

input = sys.stdin.readline

def solution(honeys : List[int]) -> int:
    left = [0] * N
    right = [0] * N
    tmp = 0
    for i in range(N):
        left[i] = tmp + honeys[i]
        tmp += honeys[i]
    tmp = 0
    for i in range(N-1, -1, -1):
        right[N-i-1] = tmp + honeys[i]
        tmp += honeys[i]

    # left, left
    left_left = 0
    for i in range(1, N):
        left_left = max(left_left, 2 * left[N-1] - left[0] - left[i] - honeys[i])
    right_right = 0
    for i in range(1, N):
        right_right = max(right_right, 2 * right[N-1] - right[0] - right[i] - honeys[N-1-i])
    left_right = 0
    for i in range(1, N-1):
        # print(i , left[i] + right[N-1-i] - honeys[0] - honeys[N-1])
        left_right = max(left_right, left[i] + right[N-1-i] - honeys[0] - honeys[N-1])

    return max(left_left, right_right, left_right)
if __name__ == "__main__":
    N = int(input())
    honeys = list(map(int, input().split()))
    print(solution(honeys))

# 9+4 = 13
# 22 - 9 = 13
# 4+1+4+9 = 13+5 = 18
# 45 -9 = 36 - 
# 22 + 27 - 18 = 49 - 18 = 31 
# 9 + 18 + 8 + 1 = 36
