#include <cstdio>
#include <iostream>

int main()
{
    long long n;
    scanf("%lld", &n);
    long long a[n];
    a[0] = 1;
    a[1] = 2;
    for(int i=2; i<n; i++)
    {
        a[i] = (a[i-1] + a[i-2])%15746;
    }
    printf("%lld\n", a[n-1]);
    return 0;
}