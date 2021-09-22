'''
FF, FS, SF, SS
1. (FF, FS)는 (FF, SF)에 와야한다.
2. (SS, SF)는 (SS, FS)에 와야한다.
3. (FF, FS)중에 한 개라도 있다면, 가장 첫 곡은 (FF, FS)중에 하나여야 한다. 없다면 무시 가능

최대한 많은 곡을 실을 수 있는 정답.
1. 다 있는 경우
    (FS - SS - SF - FF) + (FS - SF) 반복
2. FF X
    (FS - SS - SF) + (FS - SF) 반복
3. SS X
    (FS - SF - FF) + (FS - SF) 반복
5. SF X
    (FF - FS - SS)
6. (FF, SS) X
    (FS - SF) 반복
8. (FF, SF) X
    (FS - SS)

4. FS X
    (FF)
7. (FF, FS) X
    (SS) or 1
9. (SS, FS) X
    (FF) or 1
10. (SS, SF) X
    (FF) or 1
11. (FS, SF) X
    (FF)
12. 3가지 다 없는 경우
    1. SS만 산 경우
        SS의 길이
    2. FF만 산 경우
        FF의 길이
    3. 나머지
        1
'''

import sys

input = sys.stdin.readline

FF, FS, SF, SS = map(int, input().split())

ans = 0
# FS가 0이 아닌경우
if FS != 0:
    ans = SS + FF + (min(SF, FS)*2)
    if FS > SF:
        ans += 1
# FF가 0이 아닌경우
elif FF != 0:
    ans = FF
# 나머지
else:
    ans = SS
    if SF != 0:
        ans += 1
print(ans)
