#include <iostream>
#include <cstdio>

int main(){
    int n;
    int a[51] = {0,}, b[51] = {0,}, c[51] = {0,};
    scanf("%d", &n);
    for(int i=0; i<n; i++){
        scanf("%d %d", &a[i], &b[i]);
    }
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(a[i]<a[j] && b[i]<b[j]) c[i] += 1;
        }
    }
    for(int i=0; i<n; i++) printf("%d ", c[i]+1);
    printf("\n");
    return 0;
}
