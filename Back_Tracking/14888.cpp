#include <cstdio>
#include <iostream>
#include <string.h>
int max, min, n;
int *number;
bool first = true;
void operate(int start, int op[], int cal,int ans)
{
    //계산하는 법
    if (start != 0)
    {
        if (cal == 0) // +
        {
            if (start == 1) // 처음부분
                ans = number[start - 1] + number[start]; 
            else
                ans = ans + number[start];
        }
        else if (cal == 1) // -
        {
            if (start == 1)
                ans = number[start - 1] - number[start]; 
            else
                ans = ans - number[start];
        }
        else if (cal == 2) // *
        {
            if (start == 1)
                ans = number[start - 1] * number[start]; 
            else
                ans = ans * number[start];
        }
        else // /
        {
            if (start == 1)
                ans = number[start - 1] / number[start];
            else
                ans = ans / number[start]; 
        }
    }
    if (start == n-1) // basecase
    {
        if(first)
        {
            max = ans;
            min = ans;
            first = false;
        }
        if (ans > max) max = ans;
        if (ans < min) min = ans;
        ans = 0;
        return;
    }
    //재귀 끝
    for (int i = 0; i < 4; i++)
    {
        if (op[i]) // 0이 아니라면
        {
            op[i] = op[i] - 1;
            operate(start + 1, op, i, ans);
            op[i] = op[i] + 1;
        }
    }
}

int main()
{
    int op[4];
    scanf("%d", &n);
    number = new int[n];
    for (int i = 0; i < n; i++)
        scanf("%d", &number[i]);
    for (int i = 0; i < 4; i++)
        scanf("%d", &op[i]);
    operate(0, op, 0, 0);
    printf("%d\n%d\n", max, min);
    delete[] number;

    return 0;
}