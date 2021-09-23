import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

N = int(input())
num_li = list(map(int, input().split()))

oper_li = list(map(int, input().split()))
tmp = ['+', '-', '*', '/']
oper = []
for op, cnt in zip(tmp, oper_li):
    oper += [op]*cnt


max_ans = -sys.maxsize
min_ans = sys.maxsize
# 가능한 경우의 수
for per in permutations(oper, N-1):
    val_s = [num_li[0]]
    oper_s = []
    for idx, op in enumerate(per):
        cur = num_li[idx+1]
        if op == "+" or op == "-":
            val_s.append(cur)
            oper_s.append(op)
        else:
            tmp = val_s.pop()
            if op == "*":
                val_s.append(tmp*cur)
            else:
                val_s.append(tmp//cur)

    # 해당 경우의 수 계산
    for i in range(len(oper_s)):
        if oper_s[i] == "+":
            val_s[i+1] = val_s[i] + val_s[i+1]
        else:
            val_s[i+1] = val_s[i] - val_s[i+1]
    
    max_ans = max(max_ans, val_s[-1])
    min_ans = min(min_ans, val_s[-1])

print(max_ans)
print(min_ans)
