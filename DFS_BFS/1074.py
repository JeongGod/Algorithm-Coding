import sys

input = sys.stdin.readline



def dfs(n : int, x : int, y : int, start : int) -> int:
    if n == 1:
        # r, c가 범위에 있는지 체크
        if x <= C <= x + 1 and y <= R <= y + 1:
            return start + ((R - y) * 2) + (C - x)
        
        return None
    tmp = start
    go = 2**(n-1)

    for nx, ny in [(x, y), (x + go, y), (x, y + go), (x + go, y + go)]:
        
        if nx <= C <= nx + go and ny <= R <= ny + go:
            result = dfs(n=n-1, x=nx, y=ny, start=tmp)
            if result is not None:
                return result 
        tmp += 4**(n-1)
    

def main() -> int:
    global N, R, C
    N, R, C = map(int, input().split())
    print(dfs(N, 0, 0, 0))

if __name__ == "__main__":
    main()