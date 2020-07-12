#include <iostream>
#include <cstdio>

int main(){
    int n,a,b;
    int apart[16][16] = {0,};
    for(int i=1; i<16; i++) apart[0][i] = i;
    for(int j=1; j<16; j++){
        for(int k=1; k<16; k++){
            apart[j][k] = apart[j-1][k]+ apart[j][k-1];
        }
    }
    scanf("%d", &n);
    for(int i=0; i<n; i++){
        scanf("%d %d", &a, &b);
        printf("%d\n", apart[a][b]);
    }
    return 0;
}
