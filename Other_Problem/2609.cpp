#include <cstdio>
int main()
{
    int n,m,temp;
    int min=1,max=1;
    scanf("%d %d", &n, &m);
    if(n>m) temp=n;
    else temp = m;
    for(int i=2; i<=temp; i++)
    {
        for(;;)
        {
            if(n%i != 0 || m%i != 0) break;
            n/=i;
            m/=i;
            min *= i;
        }
    }
    max = min*n*m;
    printf("%d\n%d\n",min,max);
    return 0;
}