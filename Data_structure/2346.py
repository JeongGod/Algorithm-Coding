import sys

input = sys.stdin.readline

N = int(input())
ballons = list(enumerate(map(int, input().split()), start=1))


cur = 0
ans = []
for _ in range(N):
    """
    1. 풍선을 뺀다.
    2. 풍선을 빼고 움직이는 곳이 양수라면 (index+1) 에서 시작, 음수라면 (index-1)에서 시작
    3. mv만큼 움직인다. (나머지 연산)
    4. 반복
    """
    mv = ballons[cur][1]
    if mv > 0:
        start = cur
        mv -= 1
    else:
        start = cur - 1
        mv += 1
    # 한 칸 미리 움직였으니

    ans.append(ballons[cur][0])
    ballons.pop(cur)
    if len(ans) == N:
        break
    cur = (start + mv) % len(ballons)

print(*ans)
