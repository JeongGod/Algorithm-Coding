#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main(){
    int a,b;
    char n1[5],n2[5];
    char temp;
    scanf("%s %s", n1, n2);
    temp = n1[0];
    n1[0] = n1[2];
    n1[2] = temp;
    temp = n2[0];
    n2[0] = n2[2];
    n2[2] = temp;
    a = (n1[0]-'0')*100 +(n1[1]-'0')*10 +(n1[2]-'0');
    b = (n2[0]-'0')*100 +(n2[1]-'0')*10 +(n2[2]-'0');
    if(a>b) printf("%d\n", a);
    else printf("%d\n", b);
    return 0;
}
