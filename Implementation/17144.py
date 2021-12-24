"""
1. 미세먼지를 확산시킨다. (50*50)
    임시배열을 하나 만든다.
    해당 배열에 확산된 값을 넣는다.
    본 배열에 확산된 값을 더한다.
2. 공기를 순환시킨다.
    (x-1, 0), (x, 0)
    # 위에 부분
    1. 공기청정기의 위의 좌표(x-1, 0)를 기준으로 x-1을 계속 간다.
    2. 만약 0을 만났다면 (0, 0) 0을 기준으로 c-1까지 더한다.
    3. c-1을 만났다면 (0, c-1)을 기준으로 x까지 1씩 더한다.
    4. x을 만났다면 (x-1, c-1)을 기준으로 x-1을 한다.
    5. 만약 (x-1, 0)을 만났다면 (x-1, 1)은 0으로 만들고 그만둔다.

    # 아랫 부분
    1. (x, 0) => (r-1, 0)
    2. (r-1, 0) => (r-1, c-1)
    3. (r-1, c-1) => (x, c-1)
    4. (x, c-1) => (x, 0)
"""
import sys

input = sys.stdin.readline


def check(x, y):
    # 확산 가능한 경로
    spread_xy = []
    for gx, gy in direct:
        nx, ny = x+gx, y+gy
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != -1:
            spread_xy.append((nx, ny))
    return spread_xy


def spread_dust():
    # 미세먼지 확산
    for x in range(R):
        for y in range(C):
            if board[x][y] != 0 and board[x][y] != -1:
                spread_xy = check(x, y)
                spread_val = board[x][y] // 5
                board[x][y] -= len(spread_xy) * spread_val

                for nx, ny in spread_xy:
                    tmp_board[nx][ny] += spread_val
    for x in range(R):
        for y in range(C):
            board[x][y] += tmp_board[x][y]
            tmp_board[x][y] = 0


def circular_air():
    # 공기 회전
    # 위 회전
    for i in range(air_x-2, 0, -1):
        board[i][0] = board[i-1][0]
    for j in range(C-1):
        board[i-1][j] = board[i-1][j+1]
    for i in range(air_x-1):
        board[i][j+1] = board[i+1][j+1]
    for j in range(C-1, 1, -1):
        board[i+1][j] = board[i+1][j-1]
    board[air_x-1][1] = 0

    # 아래 회전
    for i in range(air_x+1, R-1):
        board[i][0] = board[i+1][0]
    for j in range(C-1):
        board[i+1][j] = board[i+1][j+1]
    for i in range(R-1, air_x, -1):
        board[i][j+1] = board[i-1][j+1]
    for j in range(C-1, 1, -1):
        board[i-1][j] = board[i-1][j-1]
    board[air_x][1] = 0


def main():
    for _ in range(T):
        spread_dust()
        circular_air()
    ans = 0
    for i in board:
        ans += sum(i)
    # -1인 공기청정기값 제거
    return ans + 2


if __name__ == "__main__":
    R, C, T = map(int, input().split())
    board = []
    # 공기청정기 위치 확인
    for i in range(R):
        _li = list(map(int, input().split()))
        if _li[0] == -1:
            air_x = i
        board.append(_li)

    tmp_board = [[0] * C for _ in range(R)]

    direct = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    print(main())
