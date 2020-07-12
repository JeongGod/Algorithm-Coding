#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;
int main(){
    int a=0,b=0,c=0;
    int m,chk;
    while(true){
        chk=0;
        scanf("%d %d %d", &a, &b, &c);
        if(a==0 && b==0 && c==0) break;
        if(pow(a,2)==pow(b,2)+pow(c,2)) chk=1;
        else if(pow(b,2)==pow(a,2)+pow(c,2)) chk=1;
        else if(pow(c,2)==pow(a,2)+pow(b,2)) chk=1;
        if(chk) printf("right\n");
        else printf("wrong\n");
    }
    return 0;
}
