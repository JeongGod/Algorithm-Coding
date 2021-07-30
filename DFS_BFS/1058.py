import sys
input = sys.stdin.readline

n = int(input())
friend = [list(input().rstrip()) for i in range(n)]

def dfs(f, f_list):
    for idx, nf in enumerate(friend[f]):
        if nf == 'Y':
            f_list.add(idx)
    return f_list
result = 0
for i in range(n):
    f_list = set()
    for idx, f in enumerate(friend[i]):
        if f == 'Y':
            f_list.add(idx)
            f_list = dfs(idx, f_list)
    result = max(len(f_list)-1, result)
print(result)