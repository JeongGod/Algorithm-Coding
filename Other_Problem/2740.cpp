#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;
int a_pan[102][102];
int b_pan[102][102];
int ans_pan[102][102];
int temp, big;
int main() {
    int n,m,k;
    scanf("%d %d", &n, &m);
    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            scanf("%d", &a_pan[j][i]);
        }
    }
    scanf("%d %d", &m, &k);
    for(int i=0; i<m; i++) {
        for(int j=0; j<k; j++) {
            scanf("%d", &b_pan[j][i]);
        }
    }
    // // print
    // printf("--------------\n");
    // for(int i=0; i<n; i++) {
    //     for(int j=0; j<m; j++) {
    //         printf("%d ", a_pan[j][i]);
    //     }
    //     printf("\n");
    // }
    // printf("--------------\n");
    // for(int i=0; i<m; i++) {
    //     for(int j=0; j<k; j++) {
    //         printf("%d ", b_pan[j][i]);
    //     }
    //     printf("\n");
    // }
    // printf("--------------\n");
    //계산
    for(int i=0; i<n; i++) {
        for(int j=0; j<k; j++) {
            for(int t=0; t<m; t++) {
                ans_pan[j][i] += a_pan[t][i] * b_pan[j][t];
            }
        }
    }
    for(int i=0; i<n; i++) {
        for(int j=0; j<k; j++) {
            printf("%d ", ans_pan[j][i]);
        }
        printf("\n");
    }
    return 0;
}