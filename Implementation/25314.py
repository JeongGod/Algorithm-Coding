import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    print("long " * (N//4) + "int")