#include <cstdio>
#include <algorithm>
typedef long long ll;
using namespace std;
int main(){
    int mine, need;
    ll ans;
    ll lan[10002];
    scanf("%d %d", &mine, &need);
    for(int i=0; i<mine; i++) {
        scanf("%lld" ,&lan[i]);
    }
    sort(lan, lan+mine);
    ll left = 1; // 최대 나눌 수 있는 수
    ll right = lan[mine-2]; // 최소 나눌 수 있는 수
    while(left <= right) {
        int cnt = 0;
        ll mid = (left+right)/2; // 기준
        for(int i=0; i<mine; i++) {
            cnt += lan[i]/mid;
        }
        if(cnt >= need) { // 기준을 늘린다.
            ans = mid;
            left = mid+1;
        } else { // 기준을 줄인다.
            right = mid-1;
        }
    }
    printf("%lld\n", ans);
    return 0;
}

/*
1. 기준을 잡는다
2. 기준으로 랜선을 나눠본다.
2-1. need보다 작거나 같게 나눠진다 => 기준을 늘린다.
2-2. need보다 크게 나눠진다 => 기준을 줄인다.
*/