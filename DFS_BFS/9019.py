import math
import sys
from collections import deque

input = sys.stdin.readline


def r_rotate(n):
    return ((n % 1000)*10) + (n // 1000)


def l_rotate(n):
    return (n % 10) * 1000 + n//10


def caculate(n, com):
    if com == 'D':
        return (n*2) % 10000
    elif com == 'S':
        return n-1 if n > 0 else 9999
    elif com == 'L':
        return r_rotate(n)
    elif com == 'R':
        return l_rotate(n)


coms = ['D', 'S', 'L', 'R']

T = int(input())

for _ in range(T):
    start, target = map(int, input().split())
    dq = deque([(start, "")])
    visited = [0] * 10001
    visited[start] = 1
    while dq:
        s, commands = dq.popleft()
        if s == target:
            print(commands)
            break

        for c in coms:
            new_commands = commands+c
            result = caculate(s, c)
            if not visited[result]:
                visited[result] = 1
                dq.append((result, new_commands))
