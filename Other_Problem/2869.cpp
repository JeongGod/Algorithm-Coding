#include <iostream>
#include <cstdio>

int main(){
    int a,b,n;
    int days=1;
    scanf("%d %d %d", &a,&b,&n);
    if(a!=n){
        n = n-a;
        if(a-b>n) days++;
        else{
            days += n/(a-b);
            if(n%(a-b)!=0) days++;
        }
    }
    printf("%d\n", days);
    return 0;
}
