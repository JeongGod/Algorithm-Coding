#include <iostream>
#include <string>
using namespace std;

int main() {
    string num, aftnum, sum, aftsum;
    int cnt=0;
    cin >> num;
    aftnum = num;
    while(true){
        if(aftnum.length()==1) {
            num = '0'+num;
            aftnum = '0'+aftnum;
        }

        sum = to_string((int(aftnum[0])-'0') + (int(aftnum[1])-'0'));

        if(sum.length()==1) aftsum=sum;
        else aftsum=sum[1];

        aftnum = aftnum[1]+aftsum;

        cnt++;
        if(aftnum == num){
            break;
        }
    }
    cout << cnt << '\n';

    return 0;
}
