#include <iostream>
#include <cstdio>
#include <cmath>
int main(){
    int a,b;
    scanf("%d %d", &a, &b);
    bool* arr;
    arr = new bool[b+1];
    for(int i=2; i<=b; i++){
        arr[i] = true;
    }
    for(int i=2; i<=sqrt(b); i++){
        if(arr[i]){
            for(int j=i+i; j<=b; j+=i){
                arr[j] = false;
            }
        }
    }
    for(int i=2; i<=b; i++){
        if(arr[i]) printf("%d\n", i);
    }
    return 0;
}
