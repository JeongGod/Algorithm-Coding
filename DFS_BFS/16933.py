import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
DAY, NIGHT = 1, 0


def check(x, y):
    return 0 <= x < N and 0 <= y < M


def bfs(board, n, m, k):
    visited = [[k+1] * m for _ in range(n)]
    visited[0][0] = 0
    dq = deque([(0, 0, 0)])
    cnt = 1
    while dq:
        for _ in range(len(dq)):
            walls, x, y = dq.popleft()
            if x == n-1 and y == m-1:
                return cnt
            for gx, gy in zip(dx, dy):
                nx, ny = x + gx, y + gy
                # 범위 체크
                if not check(nx, ny):
                    continue

                # 현재 벽을 부순 횟수가 더 크거나 같고 방문 횟수가 더 크다면 볼 필요가 없다.
                if visited[nx][ny] <= walls:
                    continue
                # 벽 체크
                if board[nx][ny] == 1:
                    # 벽을 부술 횟수가 남아있지 않다면 끝낸다.
                    if walls == k:
                        continue
                    # 낮밤체크
                    if cnt % 2 == NIGHT:
                        # 만약 밤이면 낮까지 기다리고 부숴야 한다.
                        dq.append((walls, x, y))
                        continue
                    else:
                        # 낮이면 바로 부술 수 있다.
                        # 현재 벽을 부순 횟수가 더 크거나 같고 방문 횟수가 크거나 같다면 볼 필요가 없다.
                        if visited[nx][ny] <= walls+1:
                            continue
                        dq.append((walls+1, nx, ny))
                        visited[nx][ny] = walls+1
                else:
                    dq.append((walls, nx, ny))
                    visited[nx][ny] = walls
        cnt += 1
    return -1


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    board = [list(map(int, input().rstrip())) for _ in range(N)]
    print(bfs(board, N, M, K))

"""
5 5 1
00010
11010
00010
01111
00100
"""
