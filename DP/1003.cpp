#include <cstdio>
int main(){
    int cnt,n;
    int num_cnt[41][2] = {0,};
    num_cnt[0][0] = 1;
    num_cnt[1][1] = 1;
    scanf("%d", &cnt);
    for(int i=0; i<cnt; i++){
        scanf("%d", &n);
        if(n==0) printf("%d %d\n", 1,0);
        else if(n==1) printf("%d %d\n", 0,1);
        else{
            for(int j=2; j<=n; j++){
                num_cnt[j][0] = num_cnt[j-1][0] + num_cnt[j-2][0];
                num_cnt[j][1] = num_cnt[j-1][1] + num_cnt[j-2][1];
            }
            printf("%d %d\n", num_cnt[n][0], num_cnt[n][1]);
        }
    }
    return 0;
}