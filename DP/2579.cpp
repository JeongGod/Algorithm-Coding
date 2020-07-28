#include <iostream>
#include <cstdio>
using namespace std;

int main(){
    int n,chk=0,ans=0;
    scanf("%d", &n);
    int stair[1001] = {0,}, score[1001] = {0,};
    for(int i=0; i<n; i++){
        scanf("%d", &stair[i]);
    }
    score[0]=stair[0];
    score[1]=stair[0]+stair[1];
    score[2]=max(stair[0]+stair[2], stair[1]+stair[2]);
    for(int i=3; i<n; i++){
        score[i] = max(score[i-3]+stair[i-1]+stair[i], score[i-2]+stair[i]);
    }
    printf("%d\n", score[n-1]);
    return 0;
}

// #include <iostream>
// #include <algorithm>
//
// using namespace std;
//
// int main()
// {
//     int N, score[300]= {0,}, dp[300]={0,};
//
//     // 데이터 입력
//     scanf("%d", &N);
//     for (int idx = 0; idx < N; idx++) {
//         scanf("%d", &score[idx]);
//     }
//
//     // 문제 해결
//     for (int idx = 0; idx < N; idx++) {
//         int case1 = score[idx], case2 = score[idx];
//         if (idx - 1 >= 0) {
//             case1 += dp[idx - 2];
//             case2 += score[idx - 1];
//             if (idx - 3 >= 0)
//                 case2 += dp[idx - 3];
//         }
//         dp[idx] = max(case1, case2);
//     }
//
//     // 결과 출력
//     printf("%d\n", dp[N-1]);
//     return 0;
// }
