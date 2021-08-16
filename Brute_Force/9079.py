'''
한 행, 한 열, 하나의 대각선
총 경우의 수: 2^9 512개.
흝어볼 경우 8가지 => visited로 처리
최대 512번의 연산이다. 가능.
'''
import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())

dir = [
  (0,1,2),(3,4,5),(6,7,8), 
  (0,3,6),(1,4,7),(2,5,8),
  (0,4,8),(2,4,6)
]

def check(a):
  if a == "TTTTTTTTT" or a == "HHHHHHHHH":
    return True
  return False

for _ in range(tc):
  board = ""
  visited = set()
  for _ in range(3):
    for x in map(str, input().rstrip().split()):
      board += x
  # BFS로 처리
  dq = deque([(board, 0)])

  visited.add(board)
  flag = True
  while dq:
    cur, result = dq.popleft()
    
    if check(cur):
      flag = False
      print(result)
      break
    
    # 8방향 다 본다.
    for idx in dir:
      next = cur
      for i in idx:
        if cur[i] == "T":
          next = next[:i] + "H" + next[i+1:]
        else:
          next = next[:i] + "T" + next[i+1:]
      if next in visited:
        continue
      dq.append((next, result+1))
      visited.add(next)
  if flag:
    print(-1)
