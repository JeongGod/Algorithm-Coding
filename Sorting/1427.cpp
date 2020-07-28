#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int main(){
    int n;
    int x[10] = {0,};
    scanf("%d", &n);
    string a = to_string(n);
    int len = a.length();
    for(int i=0; i<len; i++){ // 카운팅 정렬 사용
        x[a[i]-'0']++;
    }
    for(int i=9; i>=0; i--){
        for(int j=x[i]; j>0; j--){
            printf("%d",i);
        }
    }
    printf("\n");
    return 0;
}
