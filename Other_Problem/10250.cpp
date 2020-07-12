#include <iostream>
#include <cstdio>

int main(){
    int a,h,m,n;
    int high,width;
    scanf("%d", &a);
    for(int i=0; i<a; i++){
        scanf("%d %d %d", &h, &m, &n);
        high = n%h;
        width = n/h+1;
        if(high==0){
            high=h;
            width=n/h;
        }
        if(width<10) printf("%d0%d\n", high,width);
        else printf("%d%d\n", high,width);
    }
    return 0;
}
