#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
    int n;
    int a[1001];
    int len[1001] = {0,};
    int ans = 1;
    scanf("%d", &n);
    for(int i=0; i<n; i++) scanf("%d", &a[i]);
    len[0] = 1;
    for(int i=1; i<n; i++) // 하나하나 기준을 잡아서 처음부터 돌아본다.
    {
        len[i] = 1;
        // printf("a[%d] = %d\n", i, a[i]);
        for(int j=0; j<i; j++) // i번째를 기준으로 잡아 0부터 비교해본다.
        {
            if(a[j] < a[i]) // 애보다 작은가?
            {
                if(len[j] >= len[i]) // 이어져있는건가?
                {
                    printf("a[%d] = %d\n", j, a[j]);
                    len[i] = len[j]+1;
                }
            }
            // printf("len[%d] = %d\n", j,len[j]);
        }
        printf("\n");
        ans = max(ans, len[i]);
    }
    printf("%d\n", ans);
    return 0;
}