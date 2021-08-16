import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

chicken = [list(map(int, input().split())) for _ in range(n)]

'''
chicken[i] = i번째 사람의 치킨만족도
chicken[i][j] = i번째 사람의 j치킨에 대한 만족도
'''
max_like = 0
for elem in combinations(range(m), 3):
    like = 0
    for i in range(n):
        tmp = 0
        for chicken_idx in elem:
            tmp = max(tmp, chicken[i][chicken_idx])
        like += tmp
    max_like = max(max_like, like)
print(max_like)