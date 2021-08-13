'''
서로 다른 세 자리수만 주어진다.
100개의 질문을 한다.
전체 경우의 수 = (9*8*7)*100 비교해서 가능한 친구 +1
'''
import sys
input = sys.stdin.readline

N = int(input())
_li = [tuple(map(int, input().split())) for _ in range(N)]
tmp_ans = []
result = 0
for i in range(1,10):
    for j in range(1,10):
        if i == j:
            continue
        for k in range(1,10):
            if i == k or j == k:
                continue
            tmp = str(i)+str(j)+str(k)
            tmp_ans.append(tmp)

for tmp in tmp_ans:
    flag = True
    for target, strike, ball in _li:
        target = str(target)
        tmp_strike, tmp_ball = 0, 0
        # 스트라이크 개수
        for i in range(3):
            if tmp[i] == target[i]:
                tmp_strike += 1
            if tmp[i] in target:
                tmp_ball += 1
        # 개수가 맞지 않으면 가능한 수가 아니다.
        if tmp_strike != strike or (tmp_ball-tmp_strike) != ball:
            flag = False
            break
    if flag:
        result += 1
print(result)
