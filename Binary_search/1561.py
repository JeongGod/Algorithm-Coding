import sys

input = sys.stdin.readline

def calc(t : int, rides : list[int]) -> int:
    return sum(map(lambda x:t//x, rides))

def solution(n : int, rides : list[int]) -> int:
    max_time = n * max(rides)
    if len(rides) >= n:
        return n
    n -= len(rides)
    left, right = 0, max_time
    while left <= right:
        mid = (left + right) // 2
        if calc(mid, rides) < n:
            left = mid + 1
        else:
            right = mid - 1
    n -= calc(left-1, rides)

    for idx in range(len(rides)):
        if left % rides[idx] == 0:
            n -= 1
        if n == 0:
            return idx + 1


if __name__ == "__main__":
    N, M = map(int, input().split())
    rides = list(map(int, input().split()))
    print(solution(N, rides))
