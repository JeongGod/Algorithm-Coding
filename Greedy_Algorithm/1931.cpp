#include <cstdio>
#include <algorithm>
using namespace std;
struct CTIME{
    long long start;
    long long end;
};
bool cmp_CTIME(CTIME a, CTIME b)
{
    if(a.end == b.end) return a.start < b.start;
    return a.end < b.end;
}
int main()
{
    int n;
    CTIME conference[100001];
    int ans = 1; // conference[0]은 선택.
    int end_time;
    scanf("%d", &n);
    for(int i=0; i<n; i++) scanf("%lld %lld", &conference[i].start ,&conference[i].end);
    sort(conference, conference+n,cmp_CTIME); // 끝나는 시간을 기준으로 정렬
    end_time = conference[0].end;
    for(int i=1; i<n; i++)
    {
        // 전에 회의가 끝난 시간보다 시작 시간이 빠르다면 넘어간다.
        if(end_time > conference[i].start) continue;
        else
        {
            ans++;
            end_time = conference[i].end;
        }
    }
    // for(int i=0; i<n; i++) printf("%lld %lld\n", conference[i].start, conference[i].end);
    printf("%d\n", ans);
    return 0;
}


/*
Greedy Algorithm은 탐욕스러운 선택 조건, 최적 부분 구조 조건이 만족되어야 한다.
탐욕스러운 선택 조건(앞의 선택이 이후의 선택에 영향을 주지 않는 조건)
최적 부분 구조 조건(문제에 대한 최종 해결 방법이 부분 문제에 대해서도 또한 최적 문제 해결방법이다라는 조건)

*/