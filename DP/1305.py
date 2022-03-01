import sys

input = sys.stdin.readline

def solution(n : int, adv : str) -> int:
    match_idx = 0
    dp = [0] * n
    for idx in range(1, n):
        # 다르다면
        while match_idx > 0 and adv[idx] != adv[match_idx]:
            match_idx = dp[match_idx - 1]

        # 같다면
        if adv[idx] == adv[match_idx]:
            match_idx += 1
            dp[idx] = match_idx
    return dp[-1]

if __name__ == "__main__":
    N = int(input())
    adv = input().rstrip()
    print(N - solution(N, adv))
