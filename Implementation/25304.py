import sys
input = sys.stdin.readline

if __name__ == "__main__":
    recipt_total_amount = int(input())
    N = int(input())

    real_total_amount = 0
    for _ in range(N):
        price, cnt = map(int, input().split())
        real_total_amount += (price * cnt)
    
    if real_total_amount == recipt_total_amount:
        print("Yes")
    else:
        print("No")