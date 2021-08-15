import sys
input = sys.stdin.readline

N, K = map(int, input().split())
K_list = sorted(list(map(int, input().split())), reverse=True)

result = -1
def dfs(tmp):
    global result
    if N < int(tmp):
        return
    result = max(result, tmp)
    for num in K_list:
        dfs(tmp*10 + num)
for num in K_list:
    dfs(num)
print(result)