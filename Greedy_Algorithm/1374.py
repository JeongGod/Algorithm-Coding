import heapq
import sys

input = sys.stdin.readline

def solution(rooms):
    answer = 0
    hq = []
    for i in range(len(rooms)):
        _, start, end = rooms[i]
        heapq.heappush(hq, (end, start))
        # 회의실을 따로 쓸 수 있다면
        if start >= hq[0][0]:
            heapq.heappop(hq)
            continue
        # 만약 회의실을 같이 쓸 수 없다면
        else :
            answer += 1

    return answer


if __name__ == "__main__":
    N = int(input())
    rooms = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:x[1])
    print(solution(rooms))
