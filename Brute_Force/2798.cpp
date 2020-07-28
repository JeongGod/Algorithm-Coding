#include <iostream>
#include <cstdio>

int main(){
    int x[1000] = {0,};
    int a,b,max=0;
    scanf("%d %d", &a, &b);
    for(int i=0; i<a; i++){
        scanf("%d", &x[i]);
    }
    for(int i=0; i<a-2; i++){
        for(int j=i+1; j<a-1; j++){
            for(int k=j+1; k<a; k++){
                if(max<x[i]+x[j]+x[k] && x[i]+x[j]+x[k]<=b) max = x[i]+x[j]+x[k];
            }
        }
    }
    printf("%d\n", max);
    return 0;
}
