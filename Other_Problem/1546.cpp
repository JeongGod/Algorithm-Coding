#include <iostream>
using namespace std;

int main() {
    int num, max_score=0;
    cin >> num;
    float score[num],avg;
    for(int i=0;i<num;i++) cin >> score[i];
    for(int i=0;i<num;i++) {
        if(max_score < score[i]) max_score = score[i];
    }
    for(int i=0;i<num;i++){
        score[i] = score[i]/max_score*100;
        avg += score[i];
    }
    cout << avg/num << '\n';
    return 0;
}
