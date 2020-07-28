#include <iostream>
#include <cstdio>

int n,b;
int fib(int b){
    if(b==0) return 0;
    else if(b==1) return 1;
    else{
        return fib(b-1)+fib(b-2);
    }
}
int main(){
    scanf("%d", &n);
    printf("%d\n" ,fib(n));
    return 0;
}
