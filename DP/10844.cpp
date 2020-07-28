#include <cstdio>

int main()
{
    /*
    0,9는 1개의 계단수밖에 만들지 못 한다.
    */
    int n;
    long long ans=0;
    long long a[102][102]; // 0,9가 몇개인지 확인
    a[1][0] = 0;
    scanf("%d", &n);
    for(int i=1; i<=9; i++) a[1][i] = 1;
    for(int i=2; i<=n; i++) 
    {
        for(int j=0; j<=9; j++)
        {
            if(j==0) a[i][j] = a[i-1][j+1] % 1000000000;
            else if(j==9) a[i][j] = a[i-1][j-1] + a[i][j] % 1000000000;
            else a[i][j] = a[i-1][j-1] + a[i-1][j+1] % 1000000000;
        }
    }
    for(int i=0; i<=9; i++) 
    {
        ans += a[n][i];
        ans %= 1000000000;
    }
    printf("%lld\n", ans);
    return 0;
}