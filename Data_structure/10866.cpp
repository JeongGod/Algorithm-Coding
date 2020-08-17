#include <cstdio>
#include <cstring>
#include <deque>
using namespace std;
int main() {
    int n,temp;
    char a[15];
    deque<int> dq;
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        scanf("%s", a);
        if(strcmp(a, "push_back") == 0) {
            scanf("%d", &temp);
            dq.push_back(temp);
        } else if(strcmp(a, "push_front") == 0) {
            scanf("%d", &temp);
            dq.push_front(temp);
        } else if(strcmp(a, "pop_front") == 0) {
            if(!dq.empty()){
                printf("%d\n", dq.front());
                dq.pop_front();
            } else {
                printf("-1\n");
            }
        } else if(strcmp(a, "pop_back") == 0) {
            if(!dq.empty()){
                printf("%d\n", dq.back());
                dq.pop_back();
            } else {
                printf("-1\n");
            }
        } else if(strcmp(a, "size") == 0) {
            printf("%lu\n", dq.size());
        } else if(strcmp(a, "empty") == 0) {
            if(!dq.empty()){
                printf("0\n");
            } else {
                printf("1\n");
            }
        } else if(strcmp(a, "front") == 0) {
            if(!dq.empty()){
                printf("%d\n", dq.front());
            } else {
                printf("-1\n");
            }
        } else if(strcmp(a, "back") == 0) {
            if(!dq.empty()){
                printf("%d\n", dq.back());
            } else {
                printf("-1\n");
            }
        }       
    }
    return 0;
}