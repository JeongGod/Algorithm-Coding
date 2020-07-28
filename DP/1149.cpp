#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
    int hc;
    int ans=0;
    bool visit[3];
    scanf("%d", &hc);
    int color[hc][3];
    for(int i=0; i<hc; i++)
    {
        for(int j=0; j<3; j++)
        {
            scanf("%d", &color[i][j]);
        }
    }
    //dp로 저장해나간다.
    for(int i=1; i<hc; i++)
    {
        for(int j=0; j<3; j++)
        {
            color[i][j] = min(color[i-1][(j+1)%3] + color[i][j], color[i-1][(j+2)%3] + color[i][j]);
        }
    }
    // 그 중에서 최솟값
    ans = color[hc-1][0];
    for(int i=1; i<3; i++)
    {
        if(ans > color[hc-1][i]) ans = color[hc-1][i];
    }
    printf("%d\n", ans);
    return 0;
}