import sys

input = sys.stdin.readline

def solution(trees, grows):
    answer = 0
    grows = sorted([(idx, val) for idx, val in enumerate(grows)], key=lambda x:x[1])
    for i in range(N):
        answer += (trees[grows[i][0]] + grows[i][1]*i)
    return answer
    
if __name__ == "__main__":
    N = int(input())
    trees = list(map(int, input().split()))
    grows = list(map(int, input().split()))
    print(solution(trees, grows))
