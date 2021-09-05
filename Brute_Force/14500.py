import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
visited = set()
ans = 0

def check(ny, nx):
    if 0 <= ny < N and 0 <= nx < M:
        return True
    return False

direct = [(0,1), (0,-1), (1,0), (-1,0)]

def dfs(y, x, cnt, result):
    global ans
    if cnt == 4:
        ans = max(ans, result)
        return
    for idx in direct:
        ny, nx = y+idx[0], x+idx[1]
        if check(ny, nx) and (ny, nx) not in visited:
            visited.add((ny, nx))
            dfs(ny, nx, cnt+1, result+board[ny][nx])
            visited.remove((ny, nx))

# ㅗ ㅜ ㅓ ㅏ 모양 체크
def except_check(y, x):
    global ans
    arr = []
    for idx in direct:
        ny, nx = y+idx[0], x+idx[1]
        if check(ny, nx):
            arr.append(board[ny][nx])
    if len(arr) == 4:
        ans = max(ans, sum(arr)-min(arr)+board[y][x])
    else:
        ans = max(ans, sum(arr)+board[y][x])
for i in range(N):
    for j in range(M):
        visited.add((i,j))
        dfs(i,j, 1, board[i][j])
        except_check(i,j)
        visited.remove((i,j))

print(ans)

