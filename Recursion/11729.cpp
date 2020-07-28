#include <iostream>
#include <cstdio>

void p_h(int a, int start, int end, int to){
    if(a==1){
        printf("%d %d\n",start,end);
    }
    else{
        p_h(a-1,start,to,end);
        printf("%d %d\n", start,end);
        p_h(a-1,to,end,start);
    }
}

int hanoi(int a){
    if(a==1){
        return 1;
    }
    else{
        return 2*hanoi(a-1)+1;
    }
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%d\n", hanoi(n));
    p_h(n,1,3,2);
    return 0;
}
