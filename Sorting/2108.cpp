#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;
int main(){
    int n,x,cnt=0;
    int mid,nmany=0,many=0,range=0;
    int max=-4000,min=0,mc=1,chk=1;
    double sum=0;
    // 절댓값은 4000이 넘지 않으니, 8000으로 두었다.
    int b[8002] = {0,};
    scanf("%d", &n);
    for(int i=0; i<n; i++){
        scanf("%d", &x);
        b[x+4000]++;
    }
    for(int i=0; i<=8000; i++){
        for(int k=b[i]; k>0; k--){
            sum += i-4000;

            if(n/2 == cnt) mid = i-4000;
            cnt++;

            if(mc){
                mc=0;
                min = i-4000;
            }
            if(max<i-4000){
                max = i-4000;
            }
        }
        if(b[i]>nmany){
            nmany = b[i];
            many = i-4000;
            chk=1;
        }
        else if(b[i]==nmany && chk){
            many = i-4000;
            chk=0;
        }
    }
    printf("%d\n", int(round(sum/n)));
    printf("%d\n", mid);
    printf("%d\n", many);
    printf("%d\n", max-min);
    return 0;
}
