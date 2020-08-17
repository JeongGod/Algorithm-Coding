#include <cstdio>
#include <deque>
using namespace std;
int main() {
    int n,m;
    int temp,ans=0;
    int front_size, back_size;
    deque<int> dq;
    deque<int>::iterator iter;
    deque<int>::reverse_iterator rIter;
    scanf("%d %d", &n, &m);
    for(int i=1; i<=n; i++) dq.push_back(i);
    for(int i=0; i<m; i++) {
        scanf("%d", &temp);
        front_size = 0;
        back_size = 1;
        for(iter = dq.begin(); *iter != temp; iter++){
            front_size++;
        }
        for(rIter = dq.rbegin(); *rIter != temp; rIter++){
            back_size++;
        }
        while(dq.front() != temp) {
            if(front_size > back_size) {
                dq.push_front(dq.back());
                dq.pop_back();
            } else {
                dq.push_back(dq.front());
                dq.pop_front();
            }
        }
        ans = (front_size > back_size) ? ans += back_size : ans += front_size;
        dq.pop_front();
    }
    printf("%d\n", ans);
    return 0;
}