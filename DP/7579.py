import sys

input = sys.stdin.readline

def solution(memories : list[int], costs : list[int]):
    # dp[i][j] = i번째까지 봤을 때 j의 비용으로 만들 수 있는 최대 메모리
    max_costs = sum(costs)
    dp = [[0] * (max_costs+1) for _ in range(101)]
    # 초기값 설정
    for i in range(costs[0], max_costs+1):
        dp[0][i] = memories[0]
    
    # dp 테이블 채우기
    for i in range(1, len(memories)):
        cur_cost = costs[i]
        for j in range(0, cur_cost):
            dp[i][j] = dp[i-1][j]
        for j in range(cur_cost, max_costs+1):
            # 나를 포함시켜서 가느냐, 포함시키지 않느냐
            dp[i][j] = max(dp[i-1][j-cur_cost] + memories[i], dp[i-1][j])
    
    for j in range(max_costs+1):
        val = dp[len(memories)-1][j]
        if val >= M:
            return j

if __name__ == "__main__":
    N, M = map(int, input().split())
    memories = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    print(solution(memories, costs))
