#include <cstdio>
#include <cstring>
#include <deque>
#include <stack>
using namespace std;
int main() {
    int tc, n;
    char p[100002];
    char num[4000001];
    int res = 0, digit;
    deque<int> dq;
    
    stack<int> st; // 파싱하기 위해
    scanf("%d", &tc); // 테스트 케이스 입력
    for(int i=0; i<tc; i++) {
        dq.clear(); // 초기화
        scanf("%s %d", p, &n); //함수, 배열의 개수 입력
        scanf("%s", num); // 배열 입력

        // dq에 숫자 passing
        for(int j=1;; j++) {
            digit = 1, res = 0; // 초기화
            if(num[j] == ',' || num[j] == ']') { // pop
                while(!st.empty()) {
                    int temp = st.top();
                    st.pop();
                    res += temp*digit;
                    digit*=10;
                }
                if(res != 0) dq.push_back(res);
                if(num[j] == ']') break;
            }
            else { // push
                st.push(num[j]-'0');
            }
        }

        // 함수
        int len = strlen(p);
        bool reverse = false;
        bool error = false;
        for(int j=0; j<len; j++) {
            if(p[j] == 'R') {
                if(reverse) reverse = false; //원래 R이 입력되어있었다면
                else reverse = true; // R이 입력되어있지 않았다면
            } else if(p[j] == 'D') {
                if(!dq.empty()) {
                    if(reverse) dq.pop_back();
                    else dq.pop_front();
                } else {
                    error = true;
                    printf("error\n");
                    break;
                }
            }
            
        }

        // 출력
        deque<int>::iterator iter;
        deque<int>::reverse_iterator rIter;
        if(!error){
            printf("[");
            if(!dq.empty()){
                if(reverse) {
                    for(rIter = dq.rbegin(); rIter != dq.rend()-1; rIter++) {
                        printf("%d,", *rIter);
                    }
                    printf("%d", dq.front());
                } else {
                    for(iter = dq.begin(); iter != dq.end()-1; iter++) {
                        printf("%d,", *iter);
                    }
                    printf("%d", dq.back());
                }
            }
            printf("]\n");
        }
    }
    return 0;
}