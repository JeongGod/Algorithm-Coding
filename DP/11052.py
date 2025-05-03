import sys

input = sys.stdin.readline

if __name__ == "__main__":
    # 가격이 비싸면 높은 카드의 등급
    # 돈을 최대한 지불해서 카드 N개
    
    N = int(input())
    cards = [*map(int, input().split())]

    dp = [0]

    for i in range(1, N+1):
        dp += [cards[i-1]]
        for j in range(i, i//2 -1, -1):
            dp[i] = max(dp[i], dp[j] + dp[i - j])
    
    print(dp[N])