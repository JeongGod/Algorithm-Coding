import sys

input = sys.stdin.readline

"""
지뢰가 없는 지점 => 주변 8개의 칸에 지뢰가 몇 개 있는지 알려준다.
미리 보드판이 주어진다. 이를 활용하여 지뢰가 있는 곳을 숫자로 나타내라.
1. N*N보드를 "."으로 채워넣는다.
2. 지뢰가 있는 칸을 기억해놓는다. => 집합을 사용한다.
3. N*N보드를 채워넣는다.
"""
N = int(input())

bomb = set()

for x in range(N):
    for y, val in enumerate(input().rstrip()):
        if val == "*":
            bomb.add((x, y))
dist = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
board = []


def check(x, y):
    result = 0
    for mx, my in dist:
        if (x-mx, y-my) in bomb:
            result += 1
    return result


flag = False
for x in range(N):
    tmp = []
    for y, val in enumerate(input().rstrip()):
        if val == "x":
            # 지뢰를 밟았다면
            if (x, y) in bomb:
                flag = True
            tmp.append(str(check(x, y)))
        else:
            tmp.append(".")
    board.append(tmp)

if flag:
    for x, y in bomb:
        board[x][y] = "*"
for i in board:
    print("".join(i))
