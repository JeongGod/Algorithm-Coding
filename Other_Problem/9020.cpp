#include <iostream>
#include <cstdio>

int main(){
    int n;
    int a;
    bool* arr;
    arr = new bool[10001];
    scanf("%d", &n);
    for(int i=2;i<=10000;i++){
        arr[i] = true;
    }
    for(int i=2; i<=100; i++){
        if(arr[i]){
            for(int j=i+i; j<=10000; j+=i){
                arr[j] = false;
            }
        }
    }
    int x,y;
    int cx,cy;
    for(int i=0; i<n; i++){
        cx=1;
        cy=1;
        scanf("%d", &a);
        x = a/2;
        y = a/2;
        for(int i=2; i<=a; i++){
            if(!arr[x] || x+y!=a) x--;
            if(!arr[y] || x+y!=a) y++;
        }
        printf("%d %d\n", x,y);
    }
    return 0;
}
