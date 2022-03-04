import sys

input = sys.stdin.readline

def solution(files):
    length = len(files)
    dp = [[sys.maxsize] * length for _ in range(length)]
    for idx in range(length):
        dp[idx][idx] = 0
    
    sum_files = [0] * length
    sum_files[0] = files[0]
    for idx in range(1, length):
        sum_files[idx] = sum_files[idx-1] + files[idx]
    sum_files.append(0)

    file_range = 1
    start = 0
    for file_range in range(1, length):
        for start in range(length - file_range):
            end = start+file_range
            for mid in range(start, end):
                dp[start][end] = min(dp[start][end], dp[start][mid] + dp[mid+1][end] + sum_files[end] - sum_files[start-1])

    return dp[0][length-1]

if __name__ == "__main__":
    TC = int(input())
    for _ in range(TC):
        N = int(input())
        files = list(map(int, input().split()))
        print(solution(files))
