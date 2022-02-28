import heapq
import sys

input = sys.stdin.readline

def solution(cards : list[int]) -> int:
    answer = 0
    heapq.heapify(cards)
    while len(cards) != 1:
        result = heapq.heappop(cards) + heapq.heappop(cards)
        answer += result
        heapq.heappush(cards, result)
    return answer

if __name__ == "__main__":
    N = int(input())
    cards = [int(input()) for _ in range(N)]
    print(solution(cards))
