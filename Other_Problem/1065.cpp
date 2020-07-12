#include <iostream>
#include <cstdio>

int han(int a){
    int n=0;
    int hun,ten,won;
    for(int i=1; i<=a;i++){
        if(i<100) n++;
        else{
            hun = i/100;
            ten = (i%100)/10;
            won = (i%100)%10;
            if((hun-ten)==(ten-won)) n++;
        }
    }
    return n;
}

int main(){
    int num,ans;
    scanf("%d", &num);
    ans = han(num);
    printf("%d\n", ans);
    return 0;
}
