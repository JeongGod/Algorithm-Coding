#include <cstdio>
typedef long long ll;

int main() {
    ll pan[10002];
    ll n,k,ans;
    scanf("%lld %lld", &n, &k);
    ll left = 1;
    ll right = n*n;
    while(left<=right) {
        ll mid = (left+right)/2;
        ll cnt = 0;
        ll temp_cnt;
        for(int i=1; i<=n; i++) {
            temp_cnt = mid/i; // i*j <= mid가 만족하는 수 이므로 mid/i가 값.
            if(temp_cnt > n) temp_cnt = n;
            cnt += temp_cnt;
        }
        if(cnt >= k) {
            ans = mid;
            right = mid-1;
        } else {
            left = mid+1;
        }
    }
    printf("%lld\n", ans);
    return 0;
}