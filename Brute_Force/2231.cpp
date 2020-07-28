#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int main(){
    string a;
    int i,n,b,sum;
    int c;
    scanf("%d", &n);
    for(i=1; i<n; i++){
        sum = i;
        a = to_string(i);
        b = a.length();
        for(int j=0; j<b; j++){
            c = a[j] - '0';
            sum += c;
        }
        if(sum == n) break;
    }
    if(sum==n) printf("%d\n", i);
    else printf("0\n");
    return 0;
}
