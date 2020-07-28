#include <cstdio>
#include <iostream>

int arr[9];
bool visit[9][9];
void backtracking(int start, int num, int size, int pick)
{
    int len = start;
    if(start == size+1)
    {
        for(int i=1; i<start; i++) printf("%d ", arr[i]);
        printf("\n");
        return;
    }
    for(int i=pick; i<=num; i++) // 시작을 1부터 안하고 pick부터
    {
        arr[start] = i;
        backtracking(start+1, num, size, i); // i를 인자로 넣어준다.
        // if(!visit[start-1][i])
        // {
        //     arr[start] = i;
        //     backtracking(start+1, num, size);
        //     if(start != size) 
        //     {
        //         visit[start][i] = true; // for문이 끝난 놈에 대해서만 막는다.
        //         for(int k=start+1; k<num; k++)
        //         {
        //             for(int j=i+1; j<=num; j++) visit[k][j] = false;
        //         }
        //     }
        // }
    }
}
/* 어떻게 돌아가는지 확인. 재귀함수 안에다가 넣으면 됌.
    for(int i=1; i<start; i++) printf("%d ", arr[i]);
    printf("\n");
    printf("-----------\n");
    for(int i=1; i<=num; i++)
    {
        for(int j=1; j<=num; j++)
        {
            printf("%d ", visit[i][j]);
        }
        printf("\n");
    }
    printf("\n");
*/

int main()
{
    int n,m;
    scanf("%d %d", &n, &m);

    backtracking(1,n,m,1); // 변수하나 추가, n,m은 전역변수로 쓰면될듯.
    
    return 0;
}