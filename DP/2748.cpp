#include <cstdio>
#include <iostream>

int main()
{
    long long n;
    long long a[91] = {0,};
    scanf("%lld", &n);
    a[0] = 0;
    a[1] = 1;
    for(int i=2; i<=n; i++)
    {
        a[i] = a[i-1]+a[i-2];
    }
    printf("%lld\n", a[n]);
    
    return 0;
}