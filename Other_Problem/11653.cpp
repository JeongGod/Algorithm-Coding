#include <cstdio>
bool prime[10000001];
int main()
{
    int n;
    scanf("%d", &n);
    for(int i=0; i<=n; i++) prime[i] =true;
    // 에라토스테네스의 채
    for(int i=2; i*i<=n; i++)
    {
        if(prime[i])
        {
            for(int j=i*i; j<=n; j+=i) prime[j] = false;
        }
    }
    for(int i=2; i<=n; i++)
    {
        if(prime[i])
        {
            for(;;)
            {
                if(n%i != 0) break;
                n/=i;
                printf("%d\n", i);
            }
        }
    }
    return 0;
}
/*
소수를 구해보면
에라토스테네스 채
2면 2+2 2+2+2 2+2+2+2 ... 다 빼고
3면 3+3 3+3+3 3+3+3+3 ... 다 빼고
... 이런식으로 주어진 수 까지 진행한다.
그러면 소수가 남는다.
for(int i=2; i*i<=n; i++)
{
    while(n%i == 0)
    {
        n/=i;
        printf("%d\n",i);
    }
    if(n>1) printf("%d\n", n);
}
*/