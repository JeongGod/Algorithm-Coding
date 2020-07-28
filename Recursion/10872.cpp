#include <iostream>
#include <cstdio>

int a;

int fact(int a){
    if(a==0) return 1;
    return a*fact(a-1);
}

int main(){
    int n,ans;
    scanf("%d", &n);
    ans = fact(n);
    printf("%d\n", ans);
    return 0;
}
