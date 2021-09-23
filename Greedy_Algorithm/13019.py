'''
뒤에서부터 맞춰나가자.
'''
import sys
from collections import Counter

input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()

j = len(B)-1
cnt = 0
if Counter(A) != Counter(B):
    print("-1")
    exit()

for i in range(len(A)-1, -1, -1):
    if A[i] != B[j]:
        # 다른 부분의 개수를 센다.
        # 이 친구는 앞으로 가야 할 친구다.
        cnt += 1
        continue
    j -= 1
print(cnt)
