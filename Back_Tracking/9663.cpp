#include <cstdio>
#include <iostream>
#include <cstdlib>
int cnt = 0;
int visit[16];
bool promising(int row, int col)
{
    for(int i=1; i<row; i++)
    {
        // 같은 행에 이미 존재한다면
        if(visit[i] == col) return false;
        // 대각선에 존재하는지 안 하는지
        if(abs(visit[i] - col) == abs(i-row)) return false;
    }
    return true;
}

void n_queen(int row,int col, int num)
{
    if(row == num+1) // base case 여기까지 왔다면 정답!
    {
        cnt++;
        return;
    }
    for(int i=0; i<num; i++)
    {
        if(promising(row,col+i))
        {
            visit[row] = col+i;
            n_queen(row+1,1,num);
            visit[row] = 0; // 다시 초기화.
        }
    }
    // 유망하면 다시 재귀
    // 안된다면 그냥 return후 끝
}

int main()
{
    int n;
    scanf("%d", &n);
    n_queen(1, 1, n); // root
    printf("%d\n", cnt);
    return 0;
}