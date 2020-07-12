#include <iostream>
#include <cstdio>

int main(){
    int n,com,combefore;
    scanf("%d", &n);
    com = 7;
    if(n==1) printf("1\n");
    else if(n>1 && n<=7) printf("2\n");
    else{
        for(int i=2;;i++){
            combefore = com;
            com = 6*i+ combefore;
            if(n>combefore && n<=com){
                printf("%d\n", i+1);
                break;
            }
        }
    }
    return 0;
}
