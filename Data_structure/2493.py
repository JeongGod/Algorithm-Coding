'''
<문제>
1. 탑은 왼쪽으로만 신호를 보낸다.
2. 신호를 받는 탑 높이 > 신호를 보낸 탑 높이가 되어야 신호를 받는다.

<풀이>
시간복잡도 O(n^2)으로는 절대 안된다. 250억이 넘어간다.
stack은 생각치도 못했다..

stack[i][0] = index
stack[i][1] = height

현재 스택에 있는 top의 값과 비교하여 높이가 내가 더 크다면 pop을 하고 해당 
'''
import sys
input = sys.stdin.readline

num = int(input())
stack = []
h_list = zip(list(range(num)), list(map(int, input().split())))

ans = [0 for i in range(num)]

for top in h_list:
    # 스택이 비어있다면
    if not stack:
        stack.append(top)
    else:
        while len(stack) > 0 and stack[-1][1] < top[1]:
            tmp = stack.pop()
            ans[tmp[0]] = stack[-1][0]+1 if stack else 0
        stack.append(top)
while stack:
    tmp = stack.pop()
    ans[tmp[0]] = stack[-1][0]+1 if stack else 0

print(' '.join(map(str, ans)))