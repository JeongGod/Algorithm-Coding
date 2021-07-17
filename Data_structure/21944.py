import sys, heapq
input = sys.stdin.readline

n = int(input())

algo_dict = {}
level_dict = {}
problem = {}


problem_min_heap = []
problem_max_heap = []

for _ in range(n):
    pb_num, level, al_num = map(int, input().split())
    # solved했는지 안 했는지 check
    problem[pb_num] = [level, al_num]
    # Recommend 2를 위한 heapq
    heapq.heappush(problem_min_heap, (level, pb_num))
    heapq.heappush(problem_max_heap, (-level, -pb_num))
    # Algorithm Dict
    if algo_dict.get(al_num) is not None:
        # min_heap
        heapq.heappush(algo_dict[al_num][0], (level, pb_num))
        # max_heap
        heapq.heappush(algo_dict[al_num][1], (-level, -pb_num))
    else:
        min_heap = []
        max_heap = []
        heapq.heappush(min_heap, (level, pb_num))
        heapq.heappush(max_heap, (-level, -pb_num))
        algo_dict[al_num] = [min_heap, max_heap]
    # level Dict
    if level_dict.get(level) is not None:
        heapq.heappush(level_dict[level][0], pb_num)
        heapq.heappush(level_dict[level][1], -pb_num)
    else:
        min_heap = []
        max_heap = []
        heapq.heappush(min_heap, pb_num)
        heapq.heappush(max_heap, -pb_num)
        level_dict[level] = [min_heap, max_heap]

m = int(input())

for _ in range(m):
    command, *args = list(input().rstrip().split())
    if command == "recommend":
        al_num, x = list(map(int, args))
        if x == 1:
            top = (algo_dict[al_num][1])[0]
            while -top[0] != problem[-top[1]][0] or al_num != problem[-top[1]][1]:
                heapq.heappop(algo_dict[al_num][1])
                top = (algo_dict[al_num][1])[0]
            print(-top[1])
        else :
            top = (algo_dict[al_num][0])[0]
            while top[0] != problem[top[1]][0] or al_num != problem[top[1]][1]:
                heapq.heappop(algo_dict[al_num][0])
                top = (algo_dict[al_num][0])[0]
            print(top[1])

    elif command == "recommend2":
        x = int(args[0])
        if x == 1:
            while -problem_max_heap[0][0] != problem[-problem_max_heap[0][1]][0]:
                heapq.heappop(problem_max_heap)
            print(-problem_max_heap[0][1])    
        else:
            while problem_min_heap[0][0] != problem[problem_min_heap[0][1]][0]:
                heapq.heappop(problem_min_heap)
            print(problem_min_heap[0][1])
    elif command == "recommend3":
        x, level = list(map(int, args))
        success = False
        if x == 1:
            for lev in range(level, 101):
                if level_dict.get(lev) is not None:
                    while len(level_dict[lev][0]) > 0 and lev != problem[(level_dict[lev][0])[0]][0]:
                        heapq.heappop(level_dict[lev][0])
                    if len(level_dict[lev][0]) == 0:
                        continue
                    print((level_dict[lev][0])[0])
                    success = True
                    break
            if not success:
                print(-1)
        else :
            for lev in range(level-1, 0, -1):
                if level_dict.get(lev) is not None:
                    while len(level_dict[lev][1]) > 0 and lev != problem[-(level_dict[lev][1])[0]][0]:
                        heapq.heappop(level_dict[lev][1])
                    if len(level_dict[lev][1]) == 0:
                        continue
                    print(-(level_dict[lev][1])[0])
                    success = True
                    break
            if not success:
                print(-1)
    elif command == "add":
        pb_num, level, al_num = list(map(int, args))
        problem[pb_num] = [level, al_num]
        heapq.heappush(problem_min_heap, (level, pb_num))
        heapq.heappush(problem_max_heap, (-level, -pb_num))
        if algo_dict.get(al_num) is not None:
            # min_heap
            heapq.heappush(algo_dict[al_num][0], (level, pb_num))
            # max_heap
            heapq.heappush(algo_dict[al_num][1], (-level, -pb_num))
        else:
            min_heap = []
            max_heap = []
            heapq.heappush(min_heap, (level, pb_num))
            heapq.heappush(max_heap, (-level, -pb_num))
            algo_dict[al_num] = [min_heap, max_heap]
        # level Dict
        if level_dict.get(level) is not None:
            heapq.heappush(level_dict[level][0], pb_num)
            heapq.heappush(level_dict[level][1], -pb_num)
        else:
            min_heap = []
            max_heap = []
            heapq.heappush(min_heap, pb_num)
            heapq.heappush(max_heap, -pb_num)
            level_dict[level] = [min_heap, max_heap]
    elif command == "solved":
        pb_num = int(args[0])
        problem[pb_num] = [0, 0]