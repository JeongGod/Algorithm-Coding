#include <cstdio>
#include <algorithm>
typedef long long ll;
using namespace std;

int tree[1000002];
int main(){
    int n,m;
    ll ans;
    scanf("%d %d", &n, &m);
    for(int i=0; i<n; i++) {
        scanf("%d", &tree[i]);
    }
    sort(tree, tree+n);
    ll left = 0;
    ll right = tree[n-1]-1;
    while(left <= right) {
        ll mid = (left+right)/2;
        ll len = 0;
        for(int i=0; i<n; i++) {
            if(tree[i]-mid > 0){
                len += tree[i]-mid;
            }
        }
        if(len >= m) { // 높이를 올린다.
            ans = mid;
            left = mid+1;
        } else { // 높이를 줄인다.
            right = mid-1;
        }
    }
    printf("%lld\n", ans);
    return 0;
}