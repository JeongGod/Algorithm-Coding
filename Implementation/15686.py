import sys
from itertools import combinations
from collections import deque, defaultdict

input = sys.stdin.readline

EMPTY = 0
HOUSE = 1
CHICKEN = 2

if __name__ == "__main__":
    N, M = map(int, input().split())

    BOARD = []
    for _ in range(N):
        BOARD.append([*map(int, input().split())])
    
    chicken_points = []
    
    for i in range(N):
        for j in range(N):
            if BOARD[i][j] == CHICKEN:
                chicken_points.append((i, j))

    # 각 집별로 치킨집 거리 구하기.
    houses = defaultdict(list)
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for chicken_point in chicken_points:
        dq = deque([(*chicken_point, 0)])
        visited = set(chicken_point)
        while dq:
            x, y, dist = dq.popleft()
            if BOARD[x][y] == HOUSE:
                houses[(x, y)].append((dist, chicken_point))

            for dir in dirs:
                nx, ny = x + dir[0], y + dir[1]
                if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    dq.append((nx, ny, dist + 1))

    answer = 100_000_000
    # 폐업시킬 치킨 집 조합
    house_to_chicken = []
    for val in houses.values():
        house_to_chicken.append(sorted(val, key=lambda x: x[0]))

    for comb in combinations(chicken_points, len(chicken_points) - M):
        exit_chickens = set(comb)

        # 각 집별로 치킨집 거리 구하기
        result = 0
        for chicken_dist in house_to_chicken:
            for dist, key in chicken_dist:
                # 폐업 체크
                if key not in exit_chickens:
                    result += dist
                    break
        answer = min(answer, result)

    print(answer)
    