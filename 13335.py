import sys

input = sys.stdin.readline

if __name__ == "__main__":
    """
    1. 다리 길이만큼 걸린다.
    2. 다리의 최대 하중이상으로 트럭을 올릴수는 없다.

    queue에 트럭 하나가 들어간다.
    weight가 가능하면 계속 들어간다.
    현재 시각 - queue의 앞 트럭이 들어간 시각이 다리 길이보다 크면 나온다.
    """
    N, W, L = map(int, input().split())
    TRUCKS = [*map(int, input().split())]

    weight = 0
    bridge = []

    seconds = 0
    complete = 0
    index = 0
    head = 0
    while N > complete:
        # 트럭이 빠져 나갈 시각이 된다면
        if bridge and bridge[head] - seconds == 0:
            weight -= TRUCKS[head]
            head += 1
            complete += 1
        
        if index < N and weight + TRUCKS[index] <= L:
            # 트럭을 올린다.
            bridge.append(W + seconds)
            # 무게
            weight += TRUCKS[index]
            # 다음 트럭
            index += 1
        seconds += 1
    print(seconds)
