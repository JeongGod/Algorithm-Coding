#include <cstdio>
int main()
{
    int n,m;
    for(;;)
    {
        scanf("%d %d", &n, &m);
        if(n == 0 && m == 0) break;
        else
        {
            if(n>m && n%m==0) printf("multiple\n");
            else if(n<m && m%n==0) printf("factor\n");
            else printf("neither\n");
        }
    }
    return 0;
}