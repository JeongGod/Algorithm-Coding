#include <iostream>
#include <cstdio>
#include <cmath>
int main(){
    int a;
    int cnt=0;
    a=300000;
    bool* arr;
    arr = new bool[a+1];
    for(int i=2; i<=a; i++){
        arr[i] = true;
    }
    for(int i=2; i<=sqrt(a); i++){
        if(arr[i]){
            for(int j=i+i; j<=a; j+=i){
                arr[j] = false;
            }
        }
    }
    int n;
    while(true){
        scanf("%d", &n);
        if(n==0) break;
        cnt=0;
        for(int i=n+1; i<=2*n; i++){
            if(arr[i]) cnt++;
        }
        printf("%d\n", cnt);
    }
    return 0;
}
