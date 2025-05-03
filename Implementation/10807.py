import sys
from collections import defaultdict, Counter

input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    vs = Counter(map(int, input().split()))
    V = int(input())

    print(vs.get(V, 0))