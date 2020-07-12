#include <iostream>
#include <string>

using namespace std;

int main() {
    int cnt=0, chk=0;
    string sen,word;
    getline(cin, sen);

    for(int i=0; i<sen.length(); i++){
        if(sen[i] != ' '){
            if(chk == 0){
                chk = 1;
                cnt++;
            }
        }
        else{
            chk = 0;
        }
    }

    cout << cnt << '\n';
    return 0;
}

// string trim(string s) {
//     string r = s.erase(0,s.find_first_not_of(' '));
//     return r.erase(r.find_last_not_of(' ')+1);
// }
