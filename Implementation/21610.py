import sys
from typing import List, Set, Tuple

input = sys.stdin.readline

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def move_cloud(go : int, dist : int, cloud : List[List[int]]) -> Set[Tuple[int]]:
    gx, gy = dx[go] * dist, dy[go] * dist
    new_cloud = set()
    for idx in range(len(cloud)):
        nx, ny = cloud[idx][0] + gx, cloud[idx][1] + gy
        new_cloud.add((nx%N, ny%N))

    return new_cloud

def rainy(cloud : List[List[int]]):
    for x, y in cloud:
        board[x][y] += 1

def copy_water_bug(cloud : List[List[int]]) -> None:
    tmp_board = [[0] * N for _ in range(N)]
    def search_water(x : int, y : int) -> int:
        cnt = 0
        for idx in [1, 3, 5, 7]:
            gx, gy = dx[idx], dy[idx]
            nx, ny = x+gx, y+gy
            if not(0 <= nx < N and 0 <= ny < N):
                continue
            if board[nx][ny] >= 1:
                cnt += 1
        return cnt

    for i, j in cloud:
        tmp_board[i][j] += search_water(i, j)
    for i, j in cloud:
        board[i][j] += tmp_board[i][j]

def make_cloud(cloud : Set[Tuple[int]]) -> List[List[int]]:
    new_cloud = []
    for i in range(N):
        for j in range(N):
            if board[i][j] < 2 or (i, j) in cloud:
                continue
            board[i][j] -= 2
            new_cloud.append([i, j])
    return new_cloud

def solution(move : List[List[int]]) -> int:
    """
    1. 모든 구름이 방향으로 si칸 이동
    2. 각 구름에서 비가 내린다. 저장된 바구니의 양 + 1
    3. 구름이 모두 사라진다.
    4. 각 바구니에서 대각선방향 탐색 => 바구니의 수 만큼 물의 양 증가
    5. 3에서 사라진 구름말고 물의 양 >= 2 인 곳에서 구름생성
    """
    cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
    for go, dist in move:
        cloud = move_cloud(go-1, dist, cloud)
        rainy(cloud)
        copy_water_bug(cloud)
        cloud = make_cloud(cloud)

    return sum([sum(board[i]) for i in range(N)])


if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    move = [tuple(map(int, input().split())) for _ in range(M)]
    print(solution(move))
