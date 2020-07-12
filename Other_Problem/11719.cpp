#include <iostream>
using namespace std; /* std */

int main(){
    string str;
    while(true){
        getline(cin, str);
        if(cin.eof() == true){
            break;
        }
        cout<<str<< '\n';
    }

    return 0;
}
