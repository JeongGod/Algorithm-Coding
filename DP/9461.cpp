#include <cstdio>
#include <iostream>
long long a[1000] = {1,1,1,2,2,3,4,5};
int main()
{
    int test;
    int n;
    scanf("%d", &test);
    
    for(int i=0; i<test; i++)
    {
        scanf("%d", &n);
        for(int i=8; i<n; i++)
        {
            a[i] = a[i-1]+a[i-5];
        }
        printf("%lld\n", a[n-1]);
    }
    return 0;
}