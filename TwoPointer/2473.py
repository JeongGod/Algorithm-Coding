import sys

input = sys.stdin.readline

def solution(n : int, water : list[int]) -> list[int]:
    water.sort()
    min_val = sys.maxsize
    for start in range(n-2):
        left, right = start + 1, n-1
        while left < right:
            result = water[start] + water[left] + water[right]
            if abs(result) < min_val:
                min_val = abs(result)
                answer = [water[start], water[left], water[right]]
            if result == 0:
                return answer
            elif result < 0:
                left += 1
            else:
                right -= 1
    return answer


if __name__ == "__main__":
    N = int(input())
    water = list(map(int, input().split()))
    print(*solution(N, water))
