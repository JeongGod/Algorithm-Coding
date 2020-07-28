#include <cstdio>
#include <iostream>
#include <math.h>
// 3개를 뽑으면 나머지 3개는 정해진다.
// 그러므로 조합으로 할 수 있다.
int n, min = -1;
int ability[21][21];
bool visit[21];
int s_num[11], l_num[11];
int test=0;
void calculate()
{
    int end=0;
    int s_score = 0, l_score = 0;
    int index = 1;
    for(int i=1; i<=n; i++)
    {
        if(!visit[i]) // l_num
        {
            l_num[index++] = i;
        }
    }
    // l_num 구하기.

    for(int i = 1; i<=n/2; i++)
    {
        for(int j=1; j<=n/2; j++)
        {
            if(i != j)
            {
                s_score += ability[s_num[i]][s_num[j]];
                l_score += ability[l_num[i]][l_num[j]];
            }
        }
    }
    end = abs(s_score-l_score);
    if(min == -1 || end < min) 
    {
        min = end;
    }
    s_score = 0;
    l_score = 0;
}

void start_link(int start)
{
    if(start == (n/2)+1)
    {
        //계산하기
        calculate();
        return;
    }
    for(int i=1; i<=n; i++)
    {
        if(!visit[i])
        {
            if(s_num[start-1] < i)
            {
                s_num[start] = i; // s_num 넣는다.
                visit[i] = true;
                start_link(start+1);
                visit[i] = false;
            }
        }
        if(start==1) break;
        test++;
        // 첫번째 1이 선택되고 나머지 선택하면, 나머지는 그대로 정해져.
        // 6개중에 3개를 뽑으면 3개가 무조건 정해진다. 그래서 첫번째는 필요없다.
    }
}

int main()
{
    scanf("%d", &n);
    for(int i=1; i<=n; i++)
    {
        for(int j=1; j<=n; j++)
        {
            scanf("%d", &ability[i][j]);
        }
    }
    start_link(1);
    printf("%d\n", min);
    return 0;
}