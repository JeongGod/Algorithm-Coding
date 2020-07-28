#include <cstdio>
#include <iostream>
int *arr;
bool *visit;
void backtracking(int start, int num, int size)
{
    if(start-1 == size) // base condition
    {
        for(int i=1;i<=size;i++) printf("%d ", arr[i]);
        printf("\n");
        return;
    }
    for(int i=1; i<=num; i++)
    {
        if(!visit[i]) // 처음에는 다 false로 되어있음.
        {
            if(arr[start-1] < i) // 오름차순으로 하기위해.
            {
                visit[i] = true;
                arr[start] = i;
                backtracking(start+1, num, size); // 재귀
            }         
            visit[i] = false;
        }
    }
}


int main()
{
    int n,m;
    scanf("%d %d", &n, &m);
    arr = new int[m+1];
    visit = new bool[n+1];
    backtracking(1,n,m);
    delete[] visit;
    delete[] arr;    
    return 0;
}