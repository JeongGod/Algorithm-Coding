# 1 -> 2 , 2 -> 3 , 3 -> 7 
'''
1. 문제의 출력형태를 보니 재귀적으로 안쪽부터 괄호가 제거되는 형태를 보인다.
2. 재귀 조건을 정하자.. 어떻게 짤까..

# 풀이
괄호의 쌍 '(', ')' 의 위치를 기억한다.
for문을 돌면서 괄호를 벗긴다.
벗긴 괄호가 처음 본 식이라면, _set에 추가하고 해당 식을 다시 재귀돌린다.

ex)
(1+(2*(3+4)))

함수가 호출되는 순서대로 바뀌는 과정
- 1+(2*(3+4)) add
    - 1+2*(3+4) add
        - 1+2*3+4 add
    - 1+(2*3+4) add
        - 1+2*3+4 return
- (1+2*(3+4)) add
    - 1+2*(3+4) return
    - (1+2*3+4) add
        - 1+2*3+4 return
- (1+(2*3+4)) add
    - 1+(2*3+4) return
    - (1+2*3+4) return
'''

import sys
sys.setrecursionlimit(100000)
_set = set()
def jaegu(form):
    global _set
    stack = []
    bracket = []
    for idx, value in enumerate(form):
        if value == '(':
            stack.append(idx)
        elif value == ')':
            bracket.append((stack.pop(),idx))

    if not bracket:
        if not form in _set:
            _set.add(form)
        return

    for i,j in bracket:
        tmp = form[0:i] + form[i+1:j] + form[j+1:]
        if not tmp in _set:
            _set.add(tmp)
            jaegu(tmp)

form = sys.stdin.readline().rstrip()

start = [idx for idx, value in enumerate(form) if value == '(']
end = [idx for idx, value in enumerate(form) if value == ')']
end.reverse()

jaegu(form)

_set = sorted(_set)
for elem in _set:
    print(elem)
