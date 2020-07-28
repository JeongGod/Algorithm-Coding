#include <cstdio>
#include <iostream>
#include <string.h>

using namespace std;
int n;
int *arr;
bool *visit;
void back_tracking(int start, int num, int size)
{
    if(start == size) 
    {
        for(int i=0; i<start; i++) printf("%d ", arr[i]);
        printf("\n");
        return;// 해결책이면 끝
    }
    for(int i=1; i<=num; i++) //다 돌려
    {
        if(!visit[i])
        {
            visit[i] = true;
            arr[start] = i;
            back_tracking(start+1, num, size); // 재귀는 결국 stack.
            visit[i] = false;
        }
    }
}
/*
num = 4, size = 4
1,2,3,4
1,2,3,4부터 들어온다.
재귀로 들어오면 2,3,4가 들어오고 3,4는 for문 대기.
3,4가 들어오면 4만 for문 대기.
4까지 들어오면 start == size라서 print후 return.
그러면 4에 대한 visit은 false로 바뀐다.
그리고 3에 대한 for문이 끝이나니 대기하고있던 4가 돌아간다.
4에 대한 visit은 true로 바뀌고 다시 재귀함수
3이 들어왔을때 if문 타고, 다시 재귀로 돌지만 base 상태에 걸려 return
3,4에 대한 return은 끝.
[32]번째 줄 : 2에 대한 for문은 여기서 끝이난다. 그러면 3에 대한 for문이 들어오고 4는 대기.
여기까지가 출력되는게 1 2 3 4, 1 2 4 3이다.
*/

int main()
{
    int m;
    scanf("%d %d", &n, &m);
    arr = new int[m];
    visit = new bool[n+1];
    for(int i=0; i<n;i++ ) printf("bool = %d\n", visit[i]);
    back_tracking(0,n,m);

    return 0;
}