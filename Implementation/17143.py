import sys

input = sys.stdin.readline
go = {
    1 : (-1, 0),
    2 : (1, 0),
    3 : (0, 1),
    4 : (0, -1)
}

class Shark:
    def __init__(self, speed, dist, size):
        self.speed = speed
        self.dist = dist
        self.size = size

def fishing(col):
    for row in range(R):
        if board[row][col] is not None:
            result = board[row][col].size
            board[row][col] = None
            return result
    return 0

def check(x, y):
    return 0 <= x < R and 0 <= y < C

def move_shark(x, y, new_board):
    shark = board[x][y]


    # 위 아래
    if shark.dist == 1:
        nx = x + (-1 * shark.speed)
        # 바로 갈 수 있다면
        if 0 <= nx < R:
            cx, cy = nx, y
        # 바로 갈 수 없다면
        else:
            a, b = divmod(abs(nx), R-1)
            # 다른 방향
            if a%2 == 0:
                shark.dist += 1
                cx, cy = b, y
            else:
                cx, cy = R - 1 - b, y
    elif shark.dist == 2:
        nx = x + (1 * shark.speed)
        # 바로 갈 수 있다면
        if 0 <= nx < R:
            cx, cy = nx, y
        # 바로 갈 수 없다면
        else:
    
            a, b = divmod(nx - (R - 1), R-1)
    
            # 다른 방향
            if a%2 == 0:
                shark.dist -= 1
                cx, cy = R - 1 - b, y
            else:
                cx, cy = b, y
    # 왼쪽 오른쪽
    elif shark.dist == 3:
        ny = y + (1 * shark.speed)
        # 바로 갈 수 있다면
        if 0 <= ny < C:
            cx, cy = x, ny
        # 바로 갈 수 없다면
        else:
            a, b = divmod(ny - (C - 1), C-1)
            # 다른 방향
            if a%2 == 0:
                shark.dist += 1
                cx, cy = x, C - 1 - b
            else:
                cx, cy = x, b
    else:
        ny = y + (-1 * shark.speed)
        # 바로 갈 수 있다면
        if 0 <= ny < C:
            cx, cy = x, ny
        # 바로 갈 수 없다면
        else:
            a, b = divmod(abs(ny), C-1)
            # 다른 방향
            if a%2 == 0:
                shark.dist -= 1
                cx, cy = x, b
            else:
                cx, cy = x, C - 1 - b
    # 도착한 위치에 상어가 있는지
    if new_board[cx][cy] is not None:
        nshark = new_board[cx][cy]
        if shark.size > nshark.size:
            new_board[cx][cy] = shark
        else:
            new_board[cx][cy] = nshark
    else:
        new_board[cx][cy] = shark


if __name__ == "__main__":
    R, C, M = map(int, input().split())
    board = [[None] * C for _ in range(R)]

    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        board[r-1][c-1] = Shark(s, d, z)
    
    answer = 0
    for cur in range(C):
        answer += fishing(cur)

        new_board = [[None] * C for _ in range(R)]
        # 상어를 움직인다.
        for x in range(R):
            for y in range(C):
                if board[x][y] is None:
                    continue
                move_shark(x, y, new_board)
        
        board = new_board
    print(answer)
