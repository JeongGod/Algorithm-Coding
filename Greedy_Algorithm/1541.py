import sys

input = sys.stdin.readline

form = input().rstrip().split("-")

ans = sum(map(int, form[0].split("+")))
for f in form[1:]:
    if "+" in f:
        tmp = sum(map(int, f.split("+")))
        ans -= tmp
        continue
    ans -= int(f)
print(ans)
