import sys
from collections import deque
input = sys.stdin.readline

def rotate(index, direction):
    if direction == 1:
        A[index] = A[index][-1] + A[index][:-1]
    else:
        A[index] = A[index][1:] + A[index][0]

if __name__ == "__main__":
    A = []
    for _ in range(4):
        A.append(input().rstrip())
    
    K = int(input())
    for _ in range(K):
        N, D = map(int, input().split())

        # 확인
        rotate_list = [(N-1, D)]
        dq = deque([(N-1, D)])
        visited = {N-1}
        while dq:
            cur, dir = dq.popleft()
            # 회전할 때 맞닿은 극이 다르다면 같이 회전한다.
            for lr, idx, op_idx in [(-1, 6, 2), (1, 2, 6)]:
                # 양 옆의 톱니바퀴 확인
                next = cur + lr
                if 0 <= next < 4 and A[next][op_idx] != A[cur][idx] and next not in visited:
                    # 반대 방향
                    visited.add(next)
                    rotate_list.append((next, -dir))
                    dq.append((next, -dir))
        
        for idx, dir in rotate_list:
            rotate(idx, dir)
    
    
    print(int(A[0][0]) + int(A[1][0]) * 2 + int(A[2][0]) * 4 + int(A[3][0]) * 8)