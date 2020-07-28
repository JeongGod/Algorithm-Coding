#include <cstdio>
#include <iostream>

int arr[9];

void backtracking(int start, int num, int size)
{
    if(start == size)
    {
        for(int i=0; i<start; i++) printf("%d ", arr[i]);
        printf("\n");
        return;
    }
    for(int i=1; i<=num; i++) // 1부터 num까지 돈다.
    {
        arr[start] = i;
        backtracking(start+1, num, size); // 돌았다는 걸 표시하기위해 start
    }
}

int main()
{
    int n,m;
    scanf("%d %d", &n, &m);
    backtracking(0,n,m);
    return 0;
}