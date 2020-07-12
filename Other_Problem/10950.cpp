#include <iostream>
#include <cstdio>

int main(){
    int n,a,b,sum;
    scanf("%d", &n);
    for(int i=0; i<n; i++){
        scanf("%d %d", &a, &b);
        sum = a+b;
        printf("Case #%d: %d + %d = %d\n", i+1,a,b,sum);
    }
    return 0;
}
