#include <iostream>
#include <cstdio>
using namespace std;

int a[10001] = {0,};

int main(){
    int n,x;
    scanf("%d", &n);
    for(int i=0; i<n; i++){
        scanf("%d", &x);
        a[x]++;
    }
    for(int i=1; i<=10000; i++){
        for(int k=a[i]; k>0; k--){
            printf("%d\n", i);
        }
    }
    return 0;
}
