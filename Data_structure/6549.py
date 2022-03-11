import sys

input = sys.stdin.readline

def sol_stack(hist : list[int]) -> int:
    answer = 0
    st = []
    hist.append(0)
    hist.insert(0, -1)
    for idx in range(len(hist)):
        while st and hist[st[-1]] >= hist[idx]:
            height = hist[st.pop()]
            answer = max(answer, height * (standard - st[-1]))
        st.append(idx)
        standard = idx
    return answer


if __name__ == "__main__":
    while True:
        N, *hist = map(int, input().split())
        if N == 0:
            break
        print(sol_stack(hist))
