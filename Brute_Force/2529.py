import sys

input = sys.stdin.readline

N = int(input())
sign = list(map(str, input().rstrip().split()))

'''
최솟값 => 발견 끝
최댓값 => 발견 끝
''' 

def check(idx, prev, cur):
    if sign[idx] == '>':
        return prev > cur
    else:
        return prev < cur

result = []
visited = set()

def max_dfs(depth, ans):
    if len(result) == 1:
        return
    if depth == N:
        result.append(ans)
        return
    for num in range(9,-1,-1):
        if not num in visited and check(depth, ans[-1], num):
            visited.add(num)
            max_dfs(depth+1, ans+[num])
            visited.remove(num)

def min_dfs(depth, ans):
    if len(result) == 2:
        return
    if depth == N:
        result.append(ans)
        return
    for num in range(10):
        if not num in visited and check(depth, ans[-1], num):
            visited.add(num)
            min_dfs(depth+1, ans+[num])
            visited.remove(num)


for i in range(9,-1,-1):
    visited.add(i)
    max_dfs(0, [i])
    visited.remove(i)

for i in range(10):
    visited.add(i)
    min_dfs(0, [i])
    visited.remove(i)


for num in result:
    print(*num, sep='')
