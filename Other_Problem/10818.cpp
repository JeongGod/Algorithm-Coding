#include <iostream>
#include <cstdio>

int main(){
    int n,max,min;
    int a[1000001] = {0,};
    scanf("%d", &n);
    for(int i=0; i<n; i++){
        scanf("%d", &a[i]);
    }
    max = a[0];
    min = a[0];
    for(int i=0; i<n; i++){
        if(a[i]>max){
            max = a[i];
        }
        if(a[i]<min){
            min = a[i];
        }
    }
    printf("%d %d\n", min, max);
    return 0;
}
