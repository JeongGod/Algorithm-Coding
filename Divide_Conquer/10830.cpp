#include <cstdio>
#include <vector>
#define MOD 1000
using namespace std;
int a[6][6];

vector<vector<int> > mul(int n, long long expo) {
    vector<vector<int> > temp(6, vector<int>(6,0));
    vector<vector<int> > ans(6,vector<int>(6,0));
    if(expo == 1) { // BaseCase
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                temp[i][j] = a[i][j];
                temp[i][j] %= 1000;
            }
        }
        return temp;
    }
    
    temp = mul(n, expo/2);
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            for(int t=0; t<n; t++) {
                ans[i][j] += temp[i][t] * temp[t][j];
            }
            ans[i][j] %= 1000;
        }
    }
    if(expo%2 == 1) { // 홀수
        vector<vector<int> > temp2(6, vector<int>(6,0));
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                for(int t=0; t<n; t++) {
                    temp2[i][j] += ans[i][t] * a[t][j];
                }
                temp2[i][j] %= 1000;
            }
        }
        return temp2;
    } else { // 짝수
        return ans;
    }
}

int main() {
    int n;
    long long expo;
    vector<vector<int> > ans(6,vector<int>(6,0));
    scanf("%d %lld", &n, &expo);
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            scanf("%d", &a[i][j]);
        }
    }
    ans = mul(n,expo);
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            printf("%d ", ans[i][j]);
        }
        printf("\n");
    }
    return 0;
}