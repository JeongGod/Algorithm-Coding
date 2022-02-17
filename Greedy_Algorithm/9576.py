import sys

input = sys.stdin.readline

def solution(students : list[int]):
    visited = set()
    for a, b in students:
        while a in visited and a < b:
            a += 1
        visited.add(a)
    return len(visited)


if __name__ == "__main__":
    TC = int(input())
    for _ in range(TC):
        N, M = map(int, input().split())
        students = sorted([tuple(map(int, input().split())) for _ in range(M)], key=lambda x:(x[1]))
        print(solution(students))
