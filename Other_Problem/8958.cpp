#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main() {
    int num,score,cnt=0;
    char quiz[81];
    cin >> num;
    for(int i=0; i<num; i++){
        score=0;
        cnt=0;
        scanf("%s", quiz);
        for(int j=0; j<strlen(quiz); j++){
            if(quiz[j] == 'O'){
                cnt++;
            }
            else cnt=0;
            score += cnt;
        }
        cout << score<< '\n';
    }

    return 0;
}
