#include <iostream>
#include <cstdio>
#include <cstring>

int main(){
    int len,cnt=0;
    char dial, abc[20];
    scanf("%s", abc);
    len = strlen(abc);
    for(int i=0; i<len; i++){
        if('A'<=abc[i] && abc[i]<='C') cnt += 3;
        else if('D'<=abc[i] && abc[i]<='F') cnt += 4;
        else if('G'<=abc[i] && abc[i]<='I') cnt += 5;
        else if('J'<=abc[i] && abc[i]<='L') cnt += 6;
        else if('M'<=abc[i] && abc[i]<='O') cnt += 7;
        else if('P'<=abc[i] && abc[i]<='S') cnt += 8;
        else if('T'<=abc[i] && abc[i]<='V') cnt += 9;
        else cnt += 10;
    }
    printf("%d\n", cnt);
    return 0;
}
