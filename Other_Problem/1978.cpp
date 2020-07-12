#include <iostream>
#include <cstdio>

int main(){
    int n,cnt=0,chk;
    int a[100] = {0,};
    scanf("%d", &n);
    for(int i=0; i<n; i++){
        scanf("%d", &a[i]);
    }
    for(int i=0; i<n; i++){
        chk=0;
        if(a[i]==2) cnt++;
        else if(a[i]!=1){
            for(int j=2; j<a[i]; j++){
                if(a[i]%j==0){
                    chk=0;
                    break;
                }
                else chk=1;
            }
        }
        if(chk) cnt++;
    }
    printf("%d\n", cnt);
    return 0;
}
