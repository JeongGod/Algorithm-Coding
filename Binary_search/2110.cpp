#include <cstdio>
#include <algorithm>
using namespace std;
int loc[200002];
int main() {
    int num, goal, ans;
    scanf("%d %d", &num, &goal);
    for(int i=0; i<num; i++) {
        scanf("%d", &loc[i]);
    }
    sort(loc, loc+num);
    int left = 1; // 최소 간격
    int right = loc[num-1] - loc[0]; // 최대 간격
    int d;
    while(left <= right) {
        int cnt = 1; // loc[0]은 포함
        int mid = (left+right) / 2; // 간격 기준
        int start = loc[0]; // loc[0]은 포함이니 start
        for(int i=1; i<num; i++) {
            d = loc[i]-start;
            if(d >= mid) {
                cnt++;
                start = loc[i];
            }
        }
        if(cnt >= goal) { // 간격을 넓혀
            ans = mid;
            left = mid+1;
        } else { // 간격을 줄여
            right = mid-1;
        }
    }
    printf("%d\n", ans);
    return 0;
}

/*
이분 탐색 이용.
특정 간격 기준.
그 기준으로 공유기를 세워보자
1. 공유기의 수가 부족하다 => 간격을 줄인다.
2. 공유기의 수가 많다 => 간격을 늘린다.
3. 맞는다 => 정답
*/