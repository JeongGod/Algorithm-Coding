import sys

input = sys.stdin.readline


class Board:
    def __init__(self):
        self.board = [[0] * 4 for _ in range(6)]
        self.score = 0

    def break_block(self):
        flag = False
        for x in range(2, 6):
            cnt = 0
            for y in range(4):
                if self.board[x][y] != 0:
                    cnt += 1
            if cnt == 4:
                self.board[x] = [0, 0, 0, 0]
                self.score += 1
                flag = True
        # 먼저 점수를 냈다면 블록을 내리는 과정을 해야한다.
        if flag:
            return flag
        # 점수를 내는 과정이 없다면
        for x in range(2):
            if sum(self.board[x]) != 0:
                for cx in range(5, 1, -1):
                    self.board[cx] = self.board[cx-(2-x)]
                break
        for x in range(2):
            self.board[x] = [0, 0, 0, 0]
        return False

    def gravity(self):
        """
        1 : 세로 블록, 한 칸 블록 => 공간이 있다면 그대로 내린다.
        2 : 가로 블록 => 짝꿍을 찾아서 2칸을 보면서 공간을 본다. 가장 작은 공간있는만큼 내린다.
            만약, 짝꿍을 찾았다면 x+1칸을 한다.
        
        아래 -> 위, 왼쪽 -> 오른쪽 순으로 본다.
        """
        def check_empty_space(x, y) -> int:
            # 현재 x좌표부터 맨 밑까지 빈 공간이 몇 개 있는지 확인하는 함수
            cnt = 0
            for height in range(x+1, 6):
                if self.board[height][y] != 0:
                    break
                cnt += 1
            return cnt
        
        for x in range(4, -1, -1):
            y = 0
            while y < 4:
                if self.board[x][y] == 1:
                    go = check_empty_space(x, y)
                    self.board[x][y] = 0
                    self.board[x+go][y] = 1
                elif self.board[x][y] == 2:
                    go = min(check_empty_space(x, y), check_empty_space(x, y+1))

                    self.board[x][y], self.board[x][y+1] = 0, 0
                    self.board[x+go][y], self.board[x+go][y+1] = 2, 2
                    # 짝꿍것까지 확인했으니 1칸 더 이동
                    y += 1
                y += 1

    def insert_block(self, x, y, val):
        self.board[x][y] = val

def main() -> int:
    global green_b, blue_b
    N = int(input())
    green_b = Board()
    blue_b = Board()
    for _ in range(N):
        T, X, Y = map(int, input().split())
        
        """
        1 : 세로 블록, 한 칸 블록
        2 : 가로 블록
        """
        if T == 1:
            green_b.insert_block(0, Y, 1)
            blue_b.insert_block(0, X, 1)
            pass
        elif T == 2:
            green_b.insert_block(0, Y, 2)
            green_b.insert_block(0, Y+1, 2)
            blue_b.insert_block(0, X, 1)
            blue_b.insert_block(1, X, 1)
            pass
        elif T == 3:
            green_b.insert_block(0, Y, 1)
            green_b.insert_block(1, Y, 1)
            blue_b.insert_block(0, X, 2)
            blue_b.insert_block(0, X+1, 2)
            pass

        while True:
            green_b.gravity()
            print("green")
            for i in green_b.board:
                print(i)
            print("----------")
            if not green_b.break_block():
                break
        
        while True:
            blue_b.gravity()
            print("blue")
            for i in blue_b.board:
                print(i)
            print("----------")
            if not blue_b.break_block():
                print("break blue")
                for i in blue_b.board:
                    print(i)
                print("----------")
                break

    def cal_remain_blocks(b):
        result = 0
        for i in b.board:
            for val in i:
                if val != 0:
                    result += 1
        return result
    return green_b.score + blue_b.score, cal_remain_blocks(green_b) + cal_remain_blocks(blue_b)

if __name__ == "__main__":
    score, remain = main()
    print(score)
    print(remain)