#include <cstdio>
#include <limits.h>
#include <algorithm>
using namespace std;
int main()
{
    int tc,k;
    int file[502];
    int sum[502] ={0,};
    int dp[502][502];
    scanf("%d", &tc);
    for(int i=0; i<tc; i++) 
    {
        scanf("%d", &k);
        for(int j=1; j<=k; j++)
        {
            scanf("%d", &file[j]);
            sum[j] = sum[j-1]+file[j];
        }
        
        /* 
         * dp[1][3] = min(dp[1][3], dp[1][1]+dp[2][3]+sum(파일의 합))
         *            min(dp[1][3], dp[1][2]+dp[3][3]+sum(파일의 합))
         * dp[2][4] = min(dp[2][4], dp[2][2]+dp[3][4]+sum(파일의 합))
         *            min(dp[2][4], dp[2][3]+dp[4][4]+sum(파일의 합))
         */ 
        for(int j=1; j<k; ++j)
        {
            for(int tx=1; tx+j <=k; ++tx)
            {
                int ty = tx+j;
                dp[tx][ty] = INT_MAX;
                for(int mid=tx; mid<ty; ++mid)
                {
                    dp[tx][ty] = min(dp[tx][ty], dp[tx][mid]+dp[mid+1][ty]+sum[ty]-sum[tx-1]);
                }
            }
        }
        printf("%d\n", dp[1][k]);
    }
    return 0;
}