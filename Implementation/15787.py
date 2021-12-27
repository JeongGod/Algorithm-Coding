import sys

input = sys.stdin.readline

N, M = map(int, input().split())

commands = [tuple(map(int, input().split())) for _ in range(M)]
trains = [[0] * 20 for _ in range(N)]


def rotate(idx, go):
    if go == "back":
        for i in range(19):
            trains[idx][i] = trains[idx][i+1]
        trains[idx][19] = 0
    else:
        for i in range(19, 0, -1):
            trains[idx][i] = trains[idx][i-1]
        trains[idx][0] = 0


for idx in range(M):
    com, train_idx, *person = commands[idx]
    train_idx -= 1
    if com == 1:
        trains[train_idx][person[0]-1] = 1
    elif com == 2:
        trains[train_idx][person[0]-1] = 0
    elif com == 3:
        rotate(train_idx, "front")
    else:
        rotate(train_idx, "back")

# 은하수 건너기
ans = set()
for train in trains:
    key = "".join(map(str, train))
    ans.add(key)
print(len(ans))
