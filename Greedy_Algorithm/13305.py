import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input()) # 100,000
    roads = list(map(int, input().split()))
    oils = list(map(int, input().split()))

    min_oil = oils[0]
    ans = 0

    for road, oil in zip(roads, oils[:-1]):
        min_oil = min(min_oil, oil)
        ans += (min_oil * road)

    print(ans)