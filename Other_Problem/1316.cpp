#include <iostream>
#include <cstdio>
#include <cstring>

int main(){
    int len,lenchk,n,chk,cnt=0;
    char a[100001];
    scanf("%d", &n);
    for(int i=0; i<n; i++){
        char check[100] = {0,};
        chk=1;
        scanf("%s", a);
        len = strlen(a);
        check[0] = a[0];
        for(int j=0; j<len; j++){
            if(a[j] != a[j+1]){
                lenchk = strlen(check);
                for(int k=0; k<lenchk; k++){
                    if(a[j+1]==check[k]){
                        chk=0;
                        break;
                    }
                    else{
                        check[lenchk] = a[j+1];
                    }
                }
            }
        }
        if(chk) cnt++;
    }
    printf("%d\n", cnt);
    return 0;
}
