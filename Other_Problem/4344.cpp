#include <iostream>
using namespace std;

int main() {
    int c,student,sum,avg,cnt;
    float ans;
    int score[1001];
    cin >> c;

    for(int i=0; i<c; i++){
        sum=0;
        cnt=0;
        cin >> student;
        for(int j=0; j<student; j++) {
            cin >> score[j];
            // cout << "for문의 for문" << '\n';
            sum += score[j];
        }
        avg = sum/student;
        for(int j=0; j<student; j++){
            if(score[j]>avg) cnt++;
        }
        ans = (float)cnt/student;
        cout << fixed;
        cout.precision(3);
        cout << ans*100 << "%"<<'\n';
    }

    return 0;
}
