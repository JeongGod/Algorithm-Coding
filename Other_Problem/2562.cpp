#include <iostream>
#include <cstdio>

int main(){
    int max,n=1;
    int a[9] = {0,};
    for(int i=0; i<9; i++){
        scanf("%d", &a[i]);
    }
    max = a[0];
    for(int i=0; i<9; i++){
        if(a[i]>max){
            max = a[i];
            n=i+1;
        }
    }
    printf("%d\n%d\n", max,n);
    return 0;
}
