import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

R, C = map(int, input().split())
board = []
for i in range(R):
    board.append(list(input().rstrip()))

dist = [(-1, 1), (0, 1), (1, 1)]
answer = 0
def dfs(x, y):
    global answer
    # 도착하면 해당 얘들은 방문처리
    if y == C-1:
        answer += 1
        return True
    for gx, gy in dist:
        nx, ny = x+gx, y+gy
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != "x":
            board[nx][ny] = "x"
            if dfs(nx, ny):
                return True

for i in range(R):
    dfs(i, 0)
print(answer)