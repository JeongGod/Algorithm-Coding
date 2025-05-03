import sys
from collections import deque
input = sys.stdin.readline

APPLE = 2
SNAKE = 1
EMPTY = 0

def rotate(direction, seconds):
    if seconds not in SNAKE_MOVE_INFO:
        return direction
    
    move_info = SNAKE_MOVE_INFO.get(seconds, direction)
    if move_info == "L":
        return [-direction[1], direction[0]]
    else:
        return [direction[1], -direction[0]]


def snake():
    x, y = 0, 0
    direction = [0, 1]
    seconds = 0
    
    dq = deque([(x, y)])
    while True:
        BOARD[x][y] = SNAKE
        # 회전
        direction = rotate(direction, seconds)
        x, y = x + direction[0], y + direction[1]
        seconds += 1

        # 게임 종료
        if 0 <= x < N and 0 <= y < N and BOARD[x][y] != SNAKE:
            # 사과가 있는 경우
            if BOARD[x][y] != APPLE:
                sx, sy = dq.popleft()
                BOARD[sx][sy] = EMPTY
            dq.append((x, y))
        else:
            return seconds

if __name__ == "__main__":
    N = int(input())
    BOARD = [[EMPTY] * N for _ in range(N)]

    K = int(input())
    for _ in range(K):
        x, y = map(int, input().split())
        BOARD[x-1][y-1] = APPLE
    
    L = int(input())
    SNAKE_MOVE_INFO = {}
    for _ in range(L):
        seconds, dir = input().split()
        SNAKE_MOVE_INFO[int(seconds)] = dir

    print(snake())