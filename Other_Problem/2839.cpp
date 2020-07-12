#include <iostream>
using namespace std; /* std */

int main() {
    int salt1 = 3, salt2 = 5;
    int deliver, cnt=0;

    cin >> deliver;

    while(deliver>0){
        if(deliver%5==0){
            deliver = deliver -5;
            cnt++;
        }
        else if(deliver%3==0){
            deliver = deliver -3;
            cnt++;
        }
        else{
            if(deliver-5>0) deliver = deliver-5;
            else if(deliver-3>0) deliver = deliver-3;
            else {
                cnt=-1;
                break;
            }
            cnt++;
        }
    }
    cout<<cnt<<'\n';
    return  0;
}
