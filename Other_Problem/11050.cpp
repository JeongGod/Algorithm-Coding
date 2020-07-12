#include <cstdio>

int main(){
    int n,k,ans=1;
    scanf("%d %d", &n,&k);
    for(int i=1;i<=n;i++){
        ans *= i;
    }
    for(int i=1; i<=n; i++){
        if(i<=k) ans /= i;
        if(i<=(n-k)) ans /= i;
    }
    printf("%d\n", ans);
    return 0;
}