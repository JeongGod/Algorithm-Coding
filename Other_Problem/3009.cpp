#include <iostream>
#include <cstdio>

int main(){
    int x,y;
    int a[1001] ={0,};
    int b[1001] ={0,};
    for(int j=0; j<3; j++){
        scanf("%d %d", &x,&y);
        a[x] += 1;
        b[y] += 1;
    }
    for(int i=1; i<=1000; i++) if(a[i]==1) printf("%d ", i);
    for(int i=1; i<=1000; i++) if(b[i]==1) printf("%d\n", i);
    return 0;
}
