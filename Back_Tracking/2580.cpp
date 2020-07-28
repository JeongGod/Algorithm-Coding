#include <cstdio>
#include <iostream>
#include <string.h>
int sudo[10][10];
int num = 0;
bool found = false;
struct zero{
    int x;
    int y;
};
zero nums[81];
bool promising_tree(int promise_num,int x, int y, int pan[10][10])
{
    // 가로방향, 세로방향 있는지 없는지 판단.
    for(int i=1; i<=9; i++)
    {
        if(sudo[x][i] == promise_num) return false;
        if(sudo[i][y] == promise_num) return false;
    }
    // 1,2 ... 9이기 때문에 하나씩 낮춰준다.
    // 0,1 ... 8 라면 안해도 된다.
    x--; 
    y--;
    for(int i=(x/3)*3 +1; i <= 3 + (x/3)*3; i++)
    {
        for(int j=(y/3)*3 +1; j<= 3 + (y/3)*3; j++)
        {
            if(sudo[i][j] == promise_num) return false;
        }
    }

    // if(y>=1 && y<=3) // 제1,2,3구역
    // {
    //     for(int j=1; j<=3; j++)
    //     {
    //         if(x>=1 && x<=3) // 제1구역
    //         {
    //             for(int i=1; i<=3; i++)
    //             {
    //                 if(sudo[i][j] == promise_num) return false;
    //             }
    //         }
    //         else if(x>=4 && x<=6) // 제2구역
    //         {
    //             for(int i=4; i<=6; i++)
    //             {
    //                 if(sudo[i][j] == promise_num) return false;
    //             }
    //         }
    //         else // 제3구역
    //         {
    //             for(int i=7; i<=9; i++)
    //             {
    //                 if(sudo[i][j] == promise_num) return false;
    //             }
    //         }
    //     }
    // }
    // if(y>=4 && y<=6) // 제4,5,6구역
    // {
    //     for(int j=4; j<=6; j++)
    //     {
    //         if(x>=1 && x<=3) // 제4구역
    //         {
    //             for(int i=1; i<=3; i++)
    //             {
    //                 if(sudo[i][j] == promise_num) return false;
    //             }
    //         }
    //         else if(x>=4 && x<=6) // 제5구역
    //         {
    //             for(int i=4; i<=6; i++)
    //             {
    //                 if(sudo[i][j] == promise_num) return false;
    //             }
    //         }
    //         else // 제6구역
    //         {
    //             for(int i=7; i<=9; i++)
    //             {
    //                 if(sudo[i][j] == promise_num) return false;
    //             }
    //         }
    //     }
    // }
    // if(y>=7 && y<=9) // 제7,8,9구역
    // {
    //     for(int j=7; j<=9; j++)
    //     {
    //         if(x>=1 && x<=3) // 제7구역
    //         {
    //             for(int i=1; i<=3; i++)
    //             {
    //                 if(sudo[i][j] == promise_num) return false;
    //             }
    //         }
    //         else if(x>=4 && x<=6) // 제8구역
    //         {
    //             for(int i=4; i<=6; i++)
    //             {
    //                 if(sudo[i][j] == promise_num) return false;
    //             }
    //         }
    //         else // 제9구역
    //         {
    //             for(int i=7; i<=9; i++)
    //             {
    //                 if(sudo[i][j] == promise_num) return false;
    //             }
    //         }
    //     }
    // }
    return true;
}

void sudoku(int start, int pan[10][10])
{
    // 0인 친구(빈칸)만 보면된다.
    // 0인 친구에서 가로 세로만 본다.
    // 그리고 3x3박스.를 어떻게 볼것이냐. 1~3, 4~6, 7~9보면된다.
    if(found) return; // 답을 하나만 출력하기위해서
    if(start == num) // base 여기까지오면 정답!
    {
        for(int i=1; i<=9; i++)
        {
            for(int j=1; j<=9; j++)
            {
                printf("%d ", sudo[i][j]);
            }
            printf("\n");
        }
        found = true;
        return;
    }
    for(int i=1; i<=9; i++) // 유망한 놈들만 트리로 뽑아온다. 거기서 재귀를 돌려야지.
    {
        if(promising_tree(i,nums[start].x, nums[start].y, pan))
        {
            pan[nums[start].x][nums[start].y] = i;
            sudoku(start+1, pan);
        }
        // promising하다면, 다시 재귀를 돌리는거지.
    }
    // 답이 아니라면 초기화 시켜준다.
    pan[nums[start].x][nums[start].y] = 0;
}

int main()
{
    for(int i=1; i<=9; i++)
    {
        for(int j=1; j<=9; j++)
        {
            scanf("%d", &sudo[i][j]);
            if(sudo[i][j] == 0) 
            {
                nums[num].x = i; // 0인 친구의 x좌표
                nums[num++].y = j; // 0인 친구의 y좌표
            }
        }
    }
    sudoku(0, sudo);
    return 0;
}