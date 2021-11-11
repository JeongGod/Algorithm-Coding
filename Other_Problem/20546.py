"""
준현 => 살 수 있을 때 다 삼.
성민
    - 3일 연속 상승 => 전량 매도
    - 3일 연속 하락 => 전량 매수
"""
import sys

input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
JUN = [0, N]
SUNG = [0, N]
up, down = 0, 0
mi = li[0]
for i in li:
    # 준현이는 다 살 수 있는만큼 산다.
    j_buy = JUN[1] // i
    JUN[0] += j_buy
    JUN[1] -= j_buy * i
    # 성민이는 타이밍으로 산다.
    if mi < i:
        up += 1
        mi = i
    else:
        up = 0
    if mi > i:
        down += 1
        mi = i
    else:
        down = 0
    if up == 3:
        SUNG[1] += SUNG[0] * i
        SUNG[0] = 0
    if down >= 3:
        if SUNG[1] - SUNG[1] // i < 0:
            continue
        s_buy = SUNG[1] // i
        SUNG[0] += s_buy
        SUNG[1] -= s_buy * i
    mi = i
if JUN[0] * li[-1] + JUN[1] == sum(SUNG):
    print("SAMESAME")
elif JUN[0] * li[-1] + JUN[1] > sum(SUNG):
    print("BNP")
else:
    print("TIMING")
