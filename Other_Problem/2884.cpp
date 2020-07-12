#include <iostream>
#include <cstdio>

int main(){
    int a,b,nam;
    scanf("%d %d", &a, &b);
    if(b<45){
        if(a==0) a = 23;
        else a -= 1;
        nam = 45-b;
        nam = 60-nam;
    }
    else nam = b-45;
    printf("%d %d\n", a , nam);
    return 0;
}
