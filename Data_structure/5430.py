import sys
from collections import deque
tc = int(sys.stdin.readline())

for _ in range(tc):
    funcs = sys.stdin.readline().strip()
    num = int(sys.stdin.readline())
    tmp = sys.stdin.readline().strip()

    if len(tmp) == 2:
        tmp = []
    else :
        tmp = list(tmp[1:-1].split(","))

    li = deque()

    for elem in tmp:
        li.append(elem)
    # 뒤집고 버리고를 설정하자.
    reverse_flag = 1
    error = 0
    for a in funcs:
        if a == "R":
            reverse_flag *= -1
        elif a == "D":
            # 에러발생
            if not li:
                error = 1
                break
            
            if reverse_flag == 1: # 정상
                li.popleft()
            else: # 거꾸로
                li.pop()
    if error:
        print("error")
    else:
        if reverse_flag == -1:
            li.reverse()
        print("[", end='')
        l = len(li)
        for i in range(l):
            if i != l-1:
                print(li[i], end=',')
            else:
                print(li[i], end='')
        print("]")
    li.clear()