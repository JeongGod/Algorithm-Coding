import sys
from collections import defaultdict, deque

input = sys.stdin.readline

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def bfs(val, pos: list):
    new_pos = []
    while pos:
        cx, cy = pos.pop()

        for dir in dirs:
            nx, ny = cx + dir[0], cy + dir[1]
            if 0 <= nx < N and 0 <= ny < N and not BOARD[nx][ny]:
                BOARD[nx][ny] = val
                new_pos.append((nx, ny))

    return new_pos

if __name__ == "__main__":
    # NxN 시험관
    # 바이러스 종류 K개
    # 바이러스 증식, 번호가 낮은 종류의 바이러스부터
    # 이미 바이러스가 있으면 증식 못함
    # S초가 지난 뒤, (X, Y)에 존재하는 바이러스 종류, 존재하지 않는다면 0
    # 가장 왼쪽 위, (1,1)

    # 바이러스 (종류, x, y)
    # 전체 방문 판
    # 종류순서대로 바이러스 BFS
    
    N, K = map(int, input().split())
    BOARD = []
    VIRUS = defaultdict(list)
    for i in range(N):
        line = [*map(int, input().split())]
        for j in range(N):
            # 바이러스 좌표
            if line[j] != 0:
                VIRUS[line[j]].append((i, j))
        BOARD.append(line)
    
    S, X, Y = map(int, input().split())

    sorted_virus = sorted(VIRUS.keys())

    early = False
    for i in range(S):
        if early:
            break
        
        early = True
        for virus_kind in sorted_virus:
            if VIRUS[virus_kind]:
                early = False
                VIRUS[virus_kind] = bfs(virus_kind, VIRUS[virus_kind])
    print(BOARD[X-1][Y-1])