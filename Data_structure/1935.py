"""
1+(2*3)-(4/5)
7-0.8 = 6.20
"""
import string
import sys

input = sys.stdin.readline

N = int(input())
form = input().rstrip()
di = dict()
for alpha in string.ascii_uppercase[:N]:
    di[alpha] = int(input())

st = []
for i in form:
    if i.isalpha():
        st.append(di[i])
    else:
        b, a = st.pop(), st.pop()

        if i == "+":
            st.append(a+b)
        elif i == "-":
            st.append(a-b)
        elif i == "*":
            st.append(a*b)
        else:
            st.append(a/b)
print(f"{st[-1]:.2f}")
