import sys

input = sys.stdin.readline

SHORT = set()
ANSWERS = []

def first_word(command):
    answer = []
    R = False
    split_commands = command.split()
    for word in split_commands:
        if not R and word[0].lower() not in SHORT:
            R = True
            answer.append(f"[{word[0]}]{word[1:]}")
            SHORT.add(word[0].lower())
        else:
            answer.append(word)

    if R:
        ANSWERS.append(" ".join(answer))
    return R

def sequential_word(command):
    for idx, c in enumerate(command):
        if c == " " or c == "\n":
            continue
        if c.lower() not in SHORT:
            ANSWERS.append(f"{command[:idx]}[{command[idx]}]{command[idx+1:-1]}")
            SHORT.add(c.lower())
            return True

    return False

if __name__ == "__main__":
    N = int(input())

    commands = []
    for _ in range(N):
        commands.append(input())
    
    for command in commands:
        # 첫 문자만 살펴본다
        if first_word(command):
            continue
        
        # 모든 단어를 차례대로 살펴본다
        if sequential_word(command):
            continue
        
        # 없다면 그냥 추가한다
        ANSWERS.append(command[:-1])
    
    for answer in ANSWERS:
        print(answer)