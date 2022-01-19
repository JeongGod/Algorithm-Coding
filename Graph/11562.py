import sys
from typing import List

input = sys.stdin.readline

def floyd(n : int, board : List) -> None:
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    board[i][j] = 0
                if board[i][j] > board[i][k] + board[k][j]:
                    board[i][j] = board[i][k] + board[k][j]
def main():
    N, M = map(int, input().split())
    board = [[sys.maxsize] * (N+1) for _ in range(N+1)]

    for _ in range(M):
        x, y, val = map(int, input().split())
        board[x][y] = 0
        # 일방통행과 양방향 통행
        if val == 0:
            board[y][x] = 1
        else:
            board[y][x] = 0
    
    floyd(n = N, board = board)
    
    K = int(input())

    for _ in range(K):
        s, d = map(int, input().split())
        print(board[s][d])


if __name__ == "__main__":
    main()
