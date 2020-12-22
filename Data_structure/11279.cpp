#include <cstdio>
#include <string.h>
int q[100005];
int size = 0;
void heap_in(int tmp);
void heap_out();
void heap_in(int tmp)
{
    size++;
    int i;
    for(i = size; i > 1; i /=2)
    {
        if(tmp > q[i/2]) {
            q[i] = q[i/2];
        } else break;
    }
    q[i] = tmp;
}

void heap_out()
{
    printf("%d\n", q[1]);
    q[1] = q[size];
    q[size--] = 0;
    int item = q[1];
    int parent = 1;
    int child = 2;
    while(child <= size)
    {
        if(q[child] < q[child+1]) child++;
        if(q[child] > item)
        {
            q[parent] = q[child];
            parent=child; child*=2;
        } else {
            break;
        }
    }
    q[parent] = item;
}

int main()
{
    /* 
     * 1. 배열에 x를 넣는다.
     * 2. 배열에서 가장 큰 값을 출력한 뒤, 그 값을 삭제한다.
     * 0 : 2번을 실행한다.
     * 그 외 자연수 : 1번을 실행한다.
     */
    int n, tmp;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &tmp);
        if (tmp == 0)
        {
            // queue_out
            if(size == 0) printf("0\n");
            else heap_out();
        }
        else
        {
            // queue_in
            heap_in(tmp);
        }
    }
    return 0;
}