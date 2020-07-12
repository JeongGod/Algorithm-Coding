#include <iostream>
#include <cstdio>
// #include <algorithm>
using namespace std;

int main(){
    int x,y,w,h;
    int ans;
    scanf("%d %d %d %d", &x,&y,&w,&h);
    ans = x;
    if(ans>y) ans=y;
    if(ans>w-x) ans=w-x;
    if(ans>h-y) ans=h-y;
    printf("%d\n", ans);
    return 0;
}
