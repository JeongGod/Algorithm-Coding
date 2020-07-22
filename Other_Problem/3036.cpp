#include <cstdio>
int gcd(int num1, int num2)
{
    if(num1%num2 == 0) return num2;
    else
    {
        return gcd(num2, num1%num2);
    }
}
int main()
{
    int n, nam;
    int a[100];
    scanf("%d", &n);
    for(int i=0; i<n; i++) scanf("%d", &a[i]);
    for(int i=1; i<n; i++)
    {
        nam = gcd(a[0],a[i]);
        printf("%d/%d\n", a[0]/nam, a[i]/nam);
    }
    return 0;
}