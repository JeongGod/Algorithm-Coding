#include <cstdio>
#include <algorithm>
using namespace std;
int dp[101][100001] = {0}; 
/* 
Segmentation Fault가 뜬다.
지역 변수는 힙메모리를 사용하고 전역 변수는 스택메모리를 사용한다.
VS에서는 힙메모리가 작기 때문에 전역 변수로 사용해야 오류가 뜨지 않는다.
*/

int main()
{
    int n,bag;
    int weight[102];
    int price[102];
    scanf("%d %d", &n, &bag);
    for(int i=1; i<=n; i++) scanf("%d %d", &weight[i], &price[i]);
    for(int i=1; i<=n; i++) // i번째 물품을 기준.
    {
        for(int w=1; w<=bag; w++) // 무게가 가능한가
        {
            // i번쨰 물품을 기준으로 담는거야. i번째는.
            // 넣을 수 있는가?
            if(weight[i] <= w) dp[i][w] = max(price[i]+dp[i-1][w-weight[i]], dp[i-1][w]);
            // 못 넣는가?
            else dp[i][w] = dp[i-1][w];
        }
    }
    printf("%d\n", dp[n][bag]);
    return 0;
}
/*
항상 dp[i-1][w] 값은 1~i-1번쨰까지 넣은 최적의 값이다.

1~i번째까지 넣을 수 있는 최적의 값을 찾는 것이다.

만약 i번째를 넣을 수 있다면 dp[i-1]부분에서 전체 무게에서 
자신이 넣을 수 있는 무게를 뺀 값(w-weight[i] => 1~i-1까지 넣은 최적의 무게)을 
dp[i-1] 찾고 그 값과 지금 현재의 price와 더한다면 그 값은 최적이 될 것이다.
그 값과 지금 dp[i-1][w]의 값과 비교하여 가장 큰 값을 dp[i][w]에 넣는다.

넣을 수 없다면, dp[i-1][w]값을 그대로 가지고 온다.
*/