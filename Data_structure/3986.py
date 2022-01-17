import sys

input = sys.stdin.readline

def check(words):
    st = [words[0]]
    for word in words[1:]:
        if len(st) == 0:
            st.append(word)
            continue
        if st[-1] == word:
            st.pop()
        else:
            st.append(word)
    if len(st) == 0:
        return True
    return False

N = int(input())
answer = 0
for _ in range(N):
    words = input().rstrip()
    if check(words):
        answer += 1
print(answer)
