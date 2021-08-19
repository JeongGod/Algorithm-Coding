'''
10문제 5지선다.
3개의 연속된 답은 같지 않게 한다.
5점 이상일 경우의 수를 구하여라.

리스트에 추가합니다.
리스트에 같은 값이 여러번 들어오는 것을 확인해야 합니다.
이 값을 어떻게 확인할 것인가요?

'''

def dfs(depth, num, dup):
    global cnt
    if depth == 10:
        s = 0
        for j in range(10):
            if li[j] == ans[j]:
                s += 1
        if s >= 5:
            cnt += 1
        return
    for i in range(1, 6):
        tmp = dup
        if num == i:
            tmp += 1
        else:
            tmp = 1
        if tmp == 3:
            continue
        li.append(i)
        dfs(depth+1, i, tmp)
        li.pop()
        
ans = list(map(int, input().split()))
li, cnt = [], 0
dfs(0, 0, 0)
print(cnt)