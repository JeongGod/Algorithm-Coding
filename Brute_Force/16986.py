'''
A -> B -> C
1. A B
    무승부일 경우 경기 진행 순서상 뒤인 사람이 이긴 것.
2. 이전 경기의 승자, 참여하지 않은 사람 진행
3. 특정 사람이 합의된 승수를 달성할 때 까지 3을 반복한다.
4. 합의된 승수를 최초로 달성한 사람이 우승

2 => i번 손동작이 이긴다.
1 => 비긴다.
0 => 진다.
'''
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
# 가위바위보 승패
rsp = [list(map(int, input().split())) for _ in range(N)]
# 경희, 민호의 가위바위보 내는 순서
rsp_list = [list(map(int, input().split())) for _ in range(2)]
rsp_list.insert(0, "jiwoo")
# 지우의 낼 수 있는 가위바위보
jiwoo = list(range(N))
# 
init_cnt = [0, 0, 0]
init_score = [0, 0, 0]
# 이기는지 지는지 판별
def go_shoot(left, right):
    if rsp[left][right] == 2:
        return True
    return False

# 승자, 남은 사람, 횟수
dq = deque([(0, 1, init_cnt, set(), init_score)])
while dq:
    first, second, cnt, visited, score = dq.popleft()
    # 우승자 결정
    if K in score:
        if score.index(K) == 0:
            print(1)
            exit()
        else:
            continue

    # 최대 하는 횟수
    if sum(cnt)//2 == (3*(K-1) + 1):
        continue

    
    if first > second:
        first, second = second, first
    fir_list, sec_list = rsp_list[first], rsp_list[second]
    
    tmp = cnt[:]
    tmp[first] += 1
    tmp[second] += 1
    if fir_list == "jiwoo":
        for idx in jiwoo:
            # 방문하지 않았다면
            if not idx in visited:
                tmp_score = score[:]
                if go_shoot(idx, sec_list[tmp[second]-1]-1):
                    tmp_score[first] += 1
                    dq.append((first, 3-(first+second), tmp, visited | {idx}, tmp_score))
                else:
                    tmp_score[second] += 1
                    dq.append((second, 3-(first+second), tmp, visited | {idx}, tmp_score))
        continue

    # 가위바위보 승자 패자 결정
    # winner가 누구인지, other가 누구인지 판별한다
    tmp_score = score[:]
    if go_shoot(fir_list[tmp[first]-1]-1, sec_list[tmp[second]-1]-1):
        tmp_score[first] += 1
        dq.append((first, 3-(first+second), tmp, visited, tmp_score))
    else :
        tmp_score[second] += 1
        dq.append((second, 3-(first+second), tmp, visited, tmp_score))
    

print(0)
