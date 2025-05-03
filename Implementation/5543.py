import sys

input = sys.stdin.readline

if __name__ == "__main__":
    A = int(input())
    B = int(input())
    C = int(input())
    burgers = [A, B, C]

    D = int(input())
    E = int(input())
    drinks = [D, E]

    ans = 4000
    for burger in burgers:
        for drink in drinks:
            ans = min(ans, burger + drink - 50)

    print(ans)