#include <cstdio>

int main() {
    int coin[101],tc,k;
    scanf("%d %d", &tc, &k);
    for(int i=0; i<tc; i++) {
        scanf("%d", &coin[i]);
    }
    int d[10003] = {0,};
    d[0] = 1;
    for(int i=0; i<tc; i++) {
        for(int j = coin[i];j<=k;j++) {
            if(j-coin[i] >= 0)
                d[j] += d[j-coin[i]];
        }
    }
    printf("%d\n", d[k]);
    return 0;
}