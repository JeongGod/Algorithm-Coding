import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    _list = list(map(int, input().split()))
    st = []
    answer = [-1] * N
    for i, target in enumerate(_list):
        while st and st[-1][0] < target:
            _, idx = st.pop()
            answer[idx] = target
        st.append((target, i))
        

    print(*answer)

if __name__ == "__main__":
    solution()
