#include <cstdio>
int main() {
    int n, k=1;
    scanf("%d", &n);
    for(int i=n; i<=n; i-=k) {
        for(int j=n; j>i; j--) {
            printf(" ");
        }
        for(int j=0; j<2*i-1; j++) {
            printf("*");
        }
        printf("\n");
        if(i==1) k*=-1;
    }
    return 0;
}