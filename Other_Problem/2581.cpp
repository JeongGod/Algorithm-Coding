#include <iostream>
#include <cstdio>
#include <cmath>
int main(){
    int a,b;
    int sum=0,min,chk=1,sosu=0;
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
    for(int i=a; i<=b; i++){
        if(arr[i]){
            sum += i;
            if(chk){
                min=i;
                chk=0;
            }
            sosu=1;
        }
    }
    if(sosu) printf("%d\n%d\n", sum,min);
    else printf("-1\n");
    return 0;
}
