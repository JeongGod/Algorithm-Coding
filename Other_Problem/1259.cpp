#include <cstdio>

int main(){
    int n;
    for(;;){
        scanf("%d", &n);
        if(n==0) break;
        int rev = 0;
        int org = n;
        for(org=n;org>0;){
            rev *= 10;
            rev += org%10;
            org /= 10;
        }
        printf((rev == n) ? "yes\n" : "no\n");
    }
    // int n;
    // for(;;){
    //     scanf("%d", &n);
    //     int a[5] = {0,};
    //     int len = 4;
    //     if(n == 0) break;
    //     a[0] = n%10;
    //     a[1] = (n%100 - a[0])/10;
    //     a[2] = (n%1000 - a[0] - (a[1]*10))/100;
    //     a[3] = (n%10000 - a[0] - (a[1]*10) - (a[2]*100))/1000;
    //     a[4] = (n%100000 - a[0] - (a[1]*10) - (a[2]*100) - (a[3]*1000))/10000;
    //     for(int i=4; i>=0; i--, len--){
    //         if(a[i]!=0) break;
    //     }
    //     switch(len)
    //     {
    //         case 4:
    //             if(a[0] == a[4] && a[1] == a[3]) printf("yes\n");
    //             else printf("no\n");
    //             break;
    //         case 3:
    //             if(a[0] == a[3] && a[1] == a[2]) printf("yes\n");
    //             else printf("no\n");
    //             break;
    //         case 2:
    //             if(a[0] == a[2]) printf("yes\n");
    //             else printf("no\n");
    //             break;
    //         case 1:
    //             if(a[0] == a[1]) printf("yes\n");
    //             else printf("no\n");
    //             break;
    //         case 0:
    //             printf("yes\n");
    //             break;
    //     }
    // }

    return 0;
}