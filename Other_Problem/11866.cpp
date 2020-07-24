#include <cstdio>
#include <cstring>
int main()
{
    int n,k,cnt=0;
    int index=0;
    scanf("%d %d", &n,&k);
    bool list_q[1005];
    int ab[1005];
    list_q[0] = true;
    for(int i=0; i<n; i++) 
    {
        cnt = 0;
        while(cnt < k)
        {
            index = (index+1)%(n+1);
            if(!list_q[index]) cnt++;
        }
        list_q[index] = true;
        ab[i] = index;
    }
    printf("<");
    for(int i=0;i<n-1;i++) printf("%d, ", ab[i]);
    printf("%d>\n", ab[n-1]);
    return 0;
}