import sys
from collections import defaultdict

input = sys.stdin.readline

def solution():
    N = int(input())
    catstr = input().rstrip()

    alpha = defaultdict(int)
    left = 0
    answer = 0
    for pointer in range(len(catstr)):
        alpha[catstr[pointer]] += 1
        if len(alpha) > N:
            answer = max(answer, pointer - left)
            while True:
                val = catstr[left]
                alpha[val] -= 1
                left += 1
                if alpha[val] == 0:
                    del alpha[val]
                    break
    answer = max(answer, len(catstr) - left)
    return answer

if __name__ == "__main__":
    print(solution())
