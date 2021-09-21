import sys

input = sys.stdin.readline

BOARD = input().rstrip().split(".")
ans = ""
for elem in BOARD:
    mod_4, rem = divmod(len(elem), 4)
    if rem%2 != 0:
        print(-1)
        exit()
    mod_2, rem = divmod(rem, 2)
    ans += "AAAA"*mod_4 + "BB"*mod_2 + "."
print(ans[:-1])

