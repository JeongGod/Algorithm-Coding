import sys
input = sys.stdin.readline

if __name__ == "__main__":
    ans = 0
    P = 0
    for _ in range(20):
        _, score, grade = input().split()
        if grade == "P":
            continue
        score = float(score)
        P += score
        match grade:
            case "A+":
                ans += (score * 4.5)
            case "A0":
                ans += (score * 4.0)
            case "B+":
                ans += (score * 3.5)
            case "B0":
                ans += (score * 3.0)
            case "C+":
                ans += (score * 2.5)
            case "C0":
                ans += (score * 2.0)
            case "D+":
                ans += (score * 1.5)
            case "D0":
                ans += (score * 1.0)
            case "F":
                pass
            case "P":
                P -= 4.0
    print(P)
    print(ans / P)
