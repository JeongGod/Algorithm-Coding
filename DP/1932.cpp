#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
    int size,ans;
    scanf("%d", &size);
    int tri[size][size];
    for(int i=0; i<size; i++)
    {
        for(int j=0; j<size; j++) tri[i][j] = 0;
    }
    //초기화
    for(int i=1; i<=size; i++)
    {
        for(int j=0; j<i; j++)
        {
            scanf("%d", &tri[i-1][j]);
        }
    }
    //입력
    for(int i=2; i<=size; i++)
    {
        for(int j=0; j<i; j++)
        {
            if(j==0) tri[i-1][j] = tri[i-2][j] + tri[i-1][j];
            else if(j==i-1) tri[i-1][j] = tri[i-2][j-1] + tri[i-1][j];
            else tri[i-1][j] = max(tri[i-2][j-1] + tri[i-1][j] , tri[i-2][j] + tri[i-1][j]);
        }
    }
    //계산
    ans = tri[size-1][0];
    for(int i=1; i<size; i++) 
    {
        if(ans < tri[size-1][i]) ans = tri[size-1][i];
    }
    printf("%d\n", ans);
    return 0;
}