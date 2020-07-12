#include <iostream>
#include <cstdio>
using namespace std;

int main(){
    int m,n;
    string a[51];
    scanf("%d %d", &m, &n);
    for(int i=0; i<m; i++){
        scanf("%s", &a[i]);
    }
    printf("\n");
    for(int i=0; i<m; i++){
        printf("%c", a[i][0]);
        printf("\n");
    }
    return 0;
}
