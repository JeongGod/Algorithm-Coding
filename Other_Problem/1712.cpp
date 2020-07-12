#include <iostream>
#include <cstdio>

int main(){
    int fix, var, price;
    int n;
    scanf("%d %d %d", &fix,&var,&price);
    if(var>=price){
        printf("-1");
    }
    else{
        n = fix/(price-var)+1;
        printf("%d\n", n);
    }

    return 0;
}
