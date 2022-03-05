import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def check(x : int, y : int) -> bool:
    return 0 <= x < N and 0 <= y < M 

def dfs(x : int, y : int, board : list[list[int]]) -> None:
    global answer, visited, dp
    # 만약에 있던 방문했던 길이라면
    if visited[x][y]:
        return dp[x][y]
    # 도착
    if x == N-1 and y == M-1:
        return 1
    # 상하좌우 살핀다.
    for gx, gy in zip(dx, dy):
        nx, ny = x + gx, y + gy
        if not check(nx, ny):
            continue
        # 값이 작은지 확인
        if board[x][y] <= board[nx][ny]:
            continue
        dp[x][y] += dfs(nx, ny, board)
    visited[x][y] = True
    return dp[x][y]
    

def solution(board : list[list[int]]) -> int:
    global answer, visited, dp
    answer = 0
    visited = [[False] * M for _ in range(N)]
    dp = [[0] * M for _ in range(N)]
    dfs(0, 0, board)
    
    return dp[0][0]

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(solution(board))
