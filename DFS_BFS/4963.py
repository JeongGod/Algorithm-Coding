import sys
input = sys.stdin.readline

dir = [(0,1), (0,-1), (1,0), (-1,0), (-1,-1), (1,1), (1,-1), (-1,1)]

def check(x, y):
    if 0 <= x < h and 0 <= y < w and board[x][y] != 0:
        return True
    return False
    
def bfs(l):
    while l:
        x,y = l.pop()
        for idx in dir:
            nx, ny = x+idx[0], y+idx[1]
            if check(nx, ny):
                l.append((nx, ny))
                board[nx][ny] = 0
    

while True:
    w, h = map(int, input().split())
    ans = 0
    if w == 0 and h == 0:
        break
    board = [list(map(int, input().split())) for i in range(h)]
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                board[i][j] = 0
                bfs([(i, j)])
                ans += 1
    print(ans)
    
