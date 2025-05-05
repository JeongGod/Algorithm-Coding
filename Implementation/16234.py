import sys
from collections import deque

input = sys.stdin.readline

def possible(x, y, person):
    # 방문 처리
    if 0 <= x < N and 0 <= y < N:
        return L <= abs(person - BOARD[x][y]) <= R

    return False


def move(all_people, all_visited):
    # 인구 이동
    people = all_people // len(all_visited)

    for x, y in all_visited:
        BOARD[x][y] = people


if __name__ == "__main__":
    N, L, R = map(int, input().split())
    BOARD = []
    for _ in range(N):
        BOARD.append([*map(int, input().split())])
    
    
    move_flag = True
    answer = 0
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while move_flag:
        total_visited = set()
        move_flag = False

        num = 0
        sum_visited = {}
        for i in range(N):
            for j in range(N):
                if (i, j) in total_visited:
                    continue
                visited = set([(i,j)])
                people = 0
                num += 1
                dq = deque([(i, j)])
                while dq:
                    x, y = dq.popleft()
                    people += BOARD[x][y]

                    for dir in dirs:
                        nx, ny = x + dir[0], y + dir[1]
                        if (nx, ny) not in visited and (nx, ny) not in total_visited and possible(nx, ny, BOARD[x][y]):
                            visited.add((nx, ny))
                            dq.append((nx, ny))
                
                sum_visited[num] = (people, visited)
                total_visited.update(visited)
                
        # 인구이동
        if num != N * N:
            move_flag = True
            for values in sum_visited.values():
                move(values[0], values[1])
        
        if move_flag:
            answer += 1
    print(answer)
            