#include <iostream>
#include <cstdio>
#include <cmath>

int main(){
    int n;
    long long x,y,d,sq1,sq2;
    long long cnt;
    scanf("%d", &n);

    for(int i=0; i<n; i++){
        scanf("%lld %lld", &x,&y);
        d = y-x;
        sq1 = sqrt(d);
        sq2 = sq1+1;
        sq1 = pow(sq1,2);
        sq2 = pow(sq2,2);
        cnt=0;
        if(d==1) cnt=1;
        else if(d==2) cnt=2;
        else if(d==3 || d==4) cnt=3;
        else{
            if(d-sq1 > sqrt(sq1)) cnt = 2*sqrt(sq1)+1;
            else if(d==sq1) cnt = 2*sqrt(sq1)-1;
            else cnt = 2*sqrt(sq1);
        }
        printf("%lld\n", cnt);
    }
    return 0;
}
