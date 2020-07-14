#include <cstdio>

int main()
{
    int n,k,cnt=0;
    int coin[11];
    scanf("%d %d", &n, &k);
    for(int i=1; i<=n; i++) scanf("%d", &coin[i]);

    for(int i=n; i>0;)
    {
        if(k >= coin[i]) // k원이 동전보다 크다면
        {
            cnt++;
            k -= coin[i];
            // printf("k = %d\ncoing[%d] = %d\n", k, i, coin[i]);
        }
        else i--;
    }
    printf("%d\n", cnt);
    return 0;
}
/*
최소의 동전 개수를 구하는 문제이지만
조건 1. "가치의 첫 번째 동전은 1로 시작한다."
조건 2. "가치의 i번째 동전은 i-1번째의 배수이다."
라는 조건으로 인해 DP로 풀지 않고 이런식으로 풀기가 가능하다.
*/