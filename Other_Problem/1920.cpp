#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;
int main(){
    int n,m,chk,cor;
    scanf("%d", &n);
    int a[n];
    for(int i=0; i<n; i++){
        scanf("%d", &a[i]);
    }
    sort(a, a+n);
    scanf("%d", &m);
    for(int i=0; i<m; i++){
        int first = 0;
        int last = n-1;
        int half = (last)/2;
        scanf("%d", &cor);
        for(;;){
            if(a[last] >= cor && a[first] <= cor){
                if(a[half] == cor)
                {
                printf("1\n");
                break;
                }
                if(first-last == 0) 
                {
                    printf("0\n");
                    break;
                }
                if(a[half] < cor)
                {
                    first = half+1;
                    half = (first + last)/2;
                }
                else 
                {
                    last = half-1;
                    half = (first + last)/2;
                }
            }
            else {
                printf("0\n");
                break;
            }
        }
    }
    /*
    binary search algorithm

    1. n/2 찾는다.
    2-1 찾았다면 1쓰고 break.
    2-2 만약 n/2가 찾는 값 보다 작다면, 
    */
    return 0;
}