import math
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

BOARD = []

for i in range(N):
    BOARD.append(list(input()))

def check(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    return False

ans = -1

for x in range(N):
    for y in range(M):
        for dx in range(-N, N):
            for dy in range(-M, M):
                # 서로 다른 칸
                if dx == 0 and dy == 0 :
                    continue
                
                tmp = ""
                cur_x, cur_y = x, y
                # 지금 dx, dy의 등차일 경우를 돌아본다.
                while check(cur_x, cur_y):
                    tmp += BOARD[cur_x][cur_y]
                    
                    if math.sqrt(int(tmp)) == int(math.sqrt(int(tmp))):
                        ans = max(ans, int(tmp))
                    cur_x += dx
                    cur_y += dy


print(ans)
