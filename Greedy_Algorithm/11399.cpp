#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    int dp[1002] = {0,};
    int time[1002];
    scanf("%d", &n);
    for(int i=0; i<n; i++) scanf("%d", &time[i]);
    sort(time, time+n);
    dp[0] = time[0];
    int ans = time[0];
    for(int i=1; i<n; i++)
    {
        dp[i] = dp[i-1]+time[i];
        ans += dp[i];
    }
    printf("%d\n", ans);
    return 0;
}
/*
오름차순으로 정렬하면 기다리는 시간이 제일 작은 순으로 정렬이 된다.
그 뒤에 시간을 dp형식으로 더해주고, 그 값들을 더해주면 답이다.
*/