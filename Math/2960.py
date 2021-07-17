import sys
input = sys.stdin.readline

n,k = map(int, input().split())
_list = [i for i in range(n+1)]

ans = 0
for idx in range(2,n+1):
    tmp = idx
    while tmp <= n and ans < k:
        if _list[tmp] != 0:
            _list[tmp] = 0
            ans += 1
        tmp += idx
    if ans == k:
        print(tmp-idx)
        break            
# import sys
# input = sys.stdin.readline

# n,k = map(int, input().split())
# prime_number = [True for i in range(n+1)]

# ans = 0
# for i in range(2,n+1):
#     if prime_number:
#         for j in range(i, n+1, i):
#             if prime_number[j]:
#                 prime_number[j] = False
#                 ans += 1
#             if ans == k:
#                 print(j)
#                 break
#     if ans == k:
#         break