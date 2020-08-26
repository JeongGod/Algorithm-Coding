#include <cstdio>
#include <vector>
#define MOD 1000000
typedef long long ll_t;

using namespace std;
vector<vector<ll_t> > first(2, vector<ll_t>(2,1));
vector<vector<ll_t> > mul(ll_t expo) {
    vector<vector<ll_t> > temp(2, vector<ll_t>(2,0));
    vector<vector<ll_t> > temp2(2, vector<ll_t>(2,0));
    vector<vector<ll_t> > ans(2, vector<ll_t>(2,0));
    if(expo == 1) {
        return first;
    }
    temp = mul(expo/2);
    for(int i=0; i<2; i++) {
        for(int j=0; j<2; j++) {
            for(int k=0; k<2; k++) {
                temp2[i][j] += temp[i][k]*temp[k][j];
            }
            temp2[i][j] %= MOD;
        }
    }
    if(expo%2) { // 홀수
        for(int i=0; i<2; i++) {
            for(int j=0; j<2; j++) {
                for(int k=0; k<2; k++) {
                    ans[i][j] += temp2[i][k]*first[k][j];
                }
                ans[i][j] %= MOD;
            }
        }
        return ans;
    } else { // 짝수
        return temp2;
    }
}

int main() {
    vector<vector<ll_t> > ans(2, vector<ll_t>(2,0));
    ll_t n;
    scanf("%lld", &n);
    first[1][1] = 0;
    if(n==1) printf("1\n");
    else {
        ans = mul(n-1);
        printf("%lld\n", ans[0][0]);
    }
    return 0;
}

/* 피보나치 행렬 곱셈

Fn = Fn-1 + Fn-2
Fn-1 = Fn-1

|  Fn  |     | 1   1 | | Fn-1 |
|      |  =  |       | |      |
| Fn-1 |     | 1   0 | | Fn-2 |

An = M*An-1로 표현 가능
   = M(M*An-2)
   = M(M(M*An-3))
   ...
   = M**n-1 * A1
*/