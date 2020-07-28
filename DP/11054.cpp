#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
    int n;
    scanf("%d", &n);
    int a[n];
    for(int i=0; i<n; i++) scanf("%d", &a[i]);
    int left_len[1002];
    int right_len[1002];
    for(int i=0; i<n; i++) // 왼쪽 기준
    {
        left_len[i] = 1;
        for(int j=0; j<i; j++) // left
        {
            if(a[i] > a[j] && left_len[j] >= left_len[i])
            {
                left_len[i] = left_len[j] + 1;
            }
        }
    }
    //왼쪽 완료
    for(int i=n-1; i>=0; i--) // 오른쪽 기준
    {
        right_len[i] = 1;
        for(int j=n-1; j>i; j--) // right
        {
            if(a[i] > a[j] && right_len[j] >= right_len[i])
            {
                right_len[i] = right_len[j] + 1;
            }
        }
    }
    // 오른쪽 완료
    int ans = left_len[0]+right_len[0];
    for(int i=0; i<n; i++)
    {
        if(ans < left_len[i]+right_len[i]) 
            ans = left_len[i]+right_len[i];
    }
    printf("%d\n", ans-1);
    return 0;
}