#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
    int a[100002], dp[100002];
    int ans, n;
    scanf("%d", &n);
    for(int i=0; i<n; i++) scanf("%d", &a[i]);
    ans = a[0];
    dp[0] = a[0];
    for(int i=1; i<n; i++)
    {
        dp[i] = max(dp[i-1]+a[i], a[i]); // dp로 더해본 값과 현재 있는 값 중 큰 값.
        if(dp[i] < 0) // 제일 큰 값이 음수라면
        {
            dp[i] = max(dp[i], a[i]); // 지금 dp와 현재 값중에 뭐가 더 큰지 비교
        }
        ans = max(dp[i], ans);
    }
    printf("%d\n", ans);
    return 0;
}
/*
DP로 계속 더한 값과 현재 있는 값을 비교하여 큰 값을 DP에다가 넣는다.
만약 DP가 음수라면, DP에 있는 음수값과 현재 있는 값을 비교하여 큰 값을 넣는다.
그리고 ans는 지금까지 더한 최고의 값(DP)으로 최신화 시켜준다.
*/