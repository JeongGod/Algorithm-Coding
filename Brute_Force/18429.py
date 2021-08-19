'''
K=4 3일이 지나면 12감소
중량증가량이 같아도 다른 키트
N일동안 1번씩 사용
중량이 500이상 유지.

N일동안 N개의 운동키트
K만큼 하루에 감소.

모든 경우의 수 => DFS로 보는게 어떨까. 처음 조건이 있기 떄문에.
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
KIT = list(map(int, input().split()))
WEIGHT = 500

ans = 0
def dfs(end, cur_weight):
    global ans
    if len(end) == N:
        ans += 1
        print(*end)
        return
    
    for idx, num in enumerate(KIT):
        if not idx in end and cur_weight+num-K >= WEIGHT:
            dfs(end + [idx], cur_weight + num - K)


dfs([], WEIGHT)
print(ans)