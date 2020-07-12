#include <iostream>
using namespace std;

int main(){
    string a;
    cin >> a;

    for(int i=0; i<a.size(); i++){
        if(i%10==0 && i!=0){
            cout <<'\n';
        }
        cout <<a[i];
    }
    cout << '\n';
    return 0;
}
