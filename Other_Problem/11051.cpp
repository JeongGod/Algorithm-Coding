#include <cstdio>
#define MOD 10007
int main()
{
    long long n,k,ans=1;
    long long dp[1001][1001];
    scanf("%lld %lld", &n, &k);
    dp[0][0] = 1;
    dp[0][1] = 0;
    for(int i=1; i<=n; i++)
    {
        dp[i][0] = 1;
        for(int j=1; j<=k; j++)
        {
            dp[i][j] = ((dp[i-1][j-1]%MOD)+(dp[i-1][j]%MOD))%MOD;
        }
    }
    for(int i=0; i<=n; i++)
    {
        for(int j=0; j<=k; j++)
        {
            printf("%lld ", dp[i][j]);
        }
        printf("\n");
    }
    printf("%lld\n", dp[n][k]);
    return 0;
}
// nCk = n-1Ck-1 + n-1Ck
// (a+b)%m = ((a%m)+(b%m))%m