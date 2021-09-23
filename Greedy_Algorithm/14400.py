'''
일차원 직선으로 생각해보자. 
여러개의 집이 있고 거리의 합을 구했을 때 최소가 되는곳에 편의점을 짓겠다고 생각하자.
그러면 가운데에다가 짓는것이 최소가 될것이다.

'''
import sys

input = sys.stdin.readline

N = int(input())
x_li = []
y_li = []
for _ in range(N):
    x, y = map(int, input().split())
    x_li.append(x); y_li.append(y)
x_li.sort(); y_li.sort()

ans = 0
tx, ty = x_li[N//2], y_li[N//2]
for ax, ay in zip(x_li, y_li):
    ans += abs(tx-ax) + abs(ty-ay)
print(ans)
