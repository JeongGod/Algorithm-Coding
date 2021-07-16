import sys, heapq
input = sys.stdin.readline

num = int(input())

problem = {}

max_heap = []
min_heap = []

for _ in range(num):
    pb, level = map(int, input().split())
    # 난이도에 문제를 추가한다.
    problem[pb] = level
    heapq.heappush(max_heap, (-level, -pb))
    heapq.heappush(min_heap, (level, pb))

# 명령어를 수행한다.
num_command = int(input())

for _ in range(num_command):
    command = input().rstrip().split()
    if command[0] == "add":
        pb, level = int(command[1]), int(command[2])
        problem[pb] = level
        heapq.heappush(max_heap, (-level, -pb))
        heapq.heappush(min_heap, (level, pb))

    elif command[0] == "recommend":
        if command[1] == "1":
            while max_heap[0][0] != -problem[-max_heap[0][1]]:
                heapq.heappop(max_heap)
            print(-max_heap[0][1])
        else:
            while min_heap[0][0] != problem[min_heap[0][1]]:
                heapq.heappop(min_heap)
            print(min_heap[0][1])

    else:
        pb = int(command[1])
        problem[pb] = 0