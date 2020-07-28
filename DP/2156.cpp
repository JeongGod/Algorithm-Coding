#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
    int n, ans;
    int temp;
    scanf("%d", &n);
    int glass_size[20000] = {0,};
    for(int i=0; i<n; i++) scanf("%d", &glass_size[i]);
    // 입력
    int drink[20000] = {0,};
    drink[0] = glass_size[0];
    drink[1] = glass_size[0]+glass_size[1];
    drink[2] = max(drink[0]+glass_size[2], glass_size[1]+glass_size[2]);
    drink[3] = max(drink[0]+glass_size[2]+glass_size[3], drink[1]+glass_size[3]);
    for(int i=4; i<n; i++)
    {
        // temp는 1칸띄워지는 것만 신경쓰는 것.
        temp = max(drink[i-3]+glass_size[i-1]+glass_size[i], drink[i-2]+glass_size[i]);
        // 1칸띄워지는 수에서 큰 것과 2칸띄워지는 것과 비교
        drink[i] = max(temp, drink[i-4]+glass_size[i-1]+glass_size[i]);
    }
    for(int i=0; i<n; i++)
    {
        printf("drink[%d] = %d\n", i, drink[i]);
    }
    ans = max(drink[n-2], drink[n-1]);
    printf("%d\n", ans);
    return 0;
}
/*
1(1만),2(1,2밟),3(1,3밟 or 2,3밟)은 기본 베이스
4번째 밟는다고 가정
=> 4-1번째 보면 1번, 3번, 4번 마시는것과
=> 4-2번째 봐서 1번, 2번, 4번 마시는게 큰지 비교
그니깐 5번째를 마신다는 가정하에 DP를 작성한다.
만약 n번째를 마셨다는 가정하에 DP를 짜고 최대값을 비교하려면
n번쨰를 마시는 것과, n-1번째를 마시고 n번째를 안 마신것에서 큰 값을 비교하여
max값을 내면 끝이다.
*/