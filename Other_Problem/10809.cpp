#include <iostream>
using namespace std;

int main(){
    string s;
    cin >> s;
    int a[s.length()], chk=0;
    int cnt[26] = {0,};
    for(int i=97; i<=122; i++){
        for(int j=0; j<s.length(); j++){
            a[j] = s[j];
            if(a[j] == i && chk==0) {
                cnt[i-97] = j;
                chk = 1;
            }
            else if(a[j] != i && chk==0) cnt[i-97] = -1;
        }
        chk=0;
    }
    for(int i=0; i<26; i++) cout << cnt[i] <<" ";
    cout << '\n';
    return 0;
}
