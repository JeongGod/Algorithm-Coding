#include <cstdio>


int main(){
    int n,m;
    scanf("%d", &n);
    for(int i=0; i<n; i++){
        scanf("%d", &m);
        int a[m];
        int b[m];
        for(int j=0; j<m; j++){
            scanf("%d", &a[j]);
        }
        int sum = 0;
        int max = a[0];
        for(int k=0; k<m; k++){
            if(a[0]>0){ //2-2
                sum += a[k];
                if(a[k] > 0){    
                    if(max < sum) max = sum;
                } else{
                    if(sum < 0) sum = 0;
                }
            } else{ //2-3
                sum += a[k];
                if(a[k] > 0){
                    if(max < sum) max = sum;
                } else{
                    if(max < a[k]) max = a[k];
                    if(sum < 0) sum =0;
                }
            }
            
        }
        printf("%d\n", max);
    }
    return 0;
}

/*
-1 -2 -3 -4 -5 100
100
1
2
-7 5 
-5 -1 -100 1
일단 a0을 max로 놓는 건 맞다. 만약 음수여도 말이다.
그 다음에
b0 = a0
b1 = b0 + a1
b2 = b1 + a2

1. for문 안에서 해결한다.

2-2 처음은 양수, 양수만 더하고 음수면 안 더해. 그렇게 max값 도출.
2-3 처음은 음수,   - 만약 음수가 계속 나온다면, 처음 값과 그 음수값을 비교해서 큰 놈
                - 양수가 나온다면, 2-2로 돌아간다.


*/