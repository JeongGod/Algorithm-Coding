#include <iostream>
using namespace std;

int main(){
    int size,sum=0;
    cin >> size;
    char number[size];
    for(int i=0; i<size; i++){
        cin >> number[i];
        sum += number[i]-'0';
    }
    cout << sum<<'\n';
    return 0;
}
