'''
3개의 소수의 합으로 이루어지는지 판단해야한다.
일단 소수를 구한다.
1000까지 소수를 구해놓고 시작하자.
에라토스테네스의 체
2의 배수에 해당하는 놈을 다 뺀다.
3의 배수 => 4, 5 ...
'''
import sys
input = sys.stdin.readline
prime = []
visited = [False for _ in range(1000)]
for i in range(2,1000):
    if not visited[i]:
        prime.append(i)
        for j in range(2*i, 1000, i):
            visited[j] = True

def check(num):
    for i in prime:
        for j in prime:
            for k in prime:
                if N == (i+j+k):
                    print(i,j,k)
                    return;
    print(0)

TC = int(input())
for _ in range(TC):
    N = int(input())
    check(N)
                    