'''
N이 20이다.
모든 경우의수는 몇일까?
20, 20C2 20C3 20C4 20C5 20C6 20C7 ... 20C20
20, 10*19, 10*19*6, 10* .. 하나당 최대 10만으로 잡아도 200만의 경우의수
충분히 브루투포스 가능
'''

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
_li = list(map(int, input().split()))
visited = [0] * N

result = 0
def dfs(ans):
    global result
    if len(ans) > 0 and sum(ans) == S:
        result += 1
    tmp = []
    for idx, num in enumerate(_li):
        if not visited[idx]:
            visited[idx] = 1
            tmp.append(idx)
            dfs(ans + [num])
    for i in tmp:
        visited[i] = 0

dfs([])
print(result)

# ygonepiece님의 풀이
# 선택, 선택하지 않은 것으로 풀었다..
# def btk(here, sum) :
#     if here == N : return 1 if sum == K else 0
#     return btk(here + 1, sum) + btk(here + 1, sum + S[here])
# print(btk(0, 0) - (1 if K == 0 else 0))
