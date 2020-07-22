#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
    long long n,m;
    long long two_ans=0;
    long long five_ans=0;
    scanf("%d %d", &n, &m);
    long long temp = n-m;
    for(long long i=2; i<=n; i*=2)
    {
        two_ans += n/i;
        two_ans -= m/i;
        two_ans -= temp/i;
    }
    for(long long i=5; i<=n; i*=5)
    {
        five_ans += n/i;
        five_ans -= m/i;
        five_ans -= temp/i;
    }
    long long ans = min(two_ans, five_ans);
    printf("%lld\n", ans);
    return 0;
}