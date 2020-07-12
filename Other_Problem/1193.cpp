#include <iostream>
#include <cstdio>

int main(){
    int i,n,bd,d=1,chk;
    int a=1,b=1,temp;
    scanf("%d", &n);
    for(i=0; d<=n; i++){
        bd = d;
        d += i;
        if(i%2==0) chk=1;
        else chk=0;
    }
    a = i-1;
    b = 1;
    for(int j=0; j<n-bd; j++){
        a--;
        b++;
    }
    if(chk==0){
        temp=a;
        a=b;
        b=temp;
    }
    printf("%d/%d\n", b,a);
    return 0;
}
