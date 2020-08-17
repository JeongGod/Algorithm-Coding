#include <cstdio>

using namespace std;
struct printer{
    int x,y;
};
int main() {
    int tc,n,m;
    int ans;
    printer a[103];
    scanf("%d", &tc);
    for(int i=0; i<tc; i++) {
        ans = 0;
        scanf("%d %d", &n,&m);
        for(int j=1; j<=n; j++) {
            scanf("%d", &a[j].x);
            a[j].y = j-1;
        }
        // 입력 끝
        int first = 1;
        int tail = n;
        int cur;
        int check=0;
        for(;;){
            for(cur = first;;) { // cur을 지금 현재 first다음으로 놓겠다.
                check = 0;
                cur = (cur+1)%(n+1);
                if(a[cur].x > a[first].x) { // 만약 cur > first라면
                    tail = (tail+1)%(n+1); // tail을 한 칸 뒤로
                    a[tail] = a[first]; // first를 뒤로 보낸다.
                    first = (first+1)%(n+1); // first를 한 칸 뒤로
                    break;
                }
                if(cur == tail) { // cur == tail이라면
                    ans++; // 내보냈으니 ++
                    if(a[first].y == m) {
                        check = 1; // 내보내는 친구가 내가 찾는것과 같다면
                    }
                    first = (first+1)%(n+1); // first를 내보낸다.
                    break;
                }
            }
            if(first == tail || check) { // 끝까지 갔거나, 찾았다면
                if(first == tail && !check) {
                    ans++; // 끝까지 갔다면 끝에서 나올때 +
                }
                printf("%d\n", ans);
                break;
            }
        }
    }
    return 0;
}