import sys

# 태그인 부분은 !.###!으로 치환하여 !로 나누었을때 태그인 문자는 .으로 시작하게 만들어 준다.
_input = list(sys.stdin.readline().rstrip().replace("<", "!.").replace(">", "!").split("!"))

stack = []
ans = ""
for _str in _input:
    if len(_str)>0 and _str[0] == ".":
        # 태그인 문자라면 그대로 출력한다.
        ans += "<"+_str[1:]+">"
    else:
        # 태그가 아닌 단어들(띄어쓰기 포함되어서 들어온다.)
        _str = " ".join([elem[::-1] for elem in _str.split()])
        ans += _str
print(ans)