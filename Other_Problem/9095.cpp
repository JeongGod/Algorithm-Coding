#include <iostream>
using namespace std;

int main(){
    int cnt, num;
    int arr[11];
    cin >> cnt;
    arr[0]=1;
    arr[1]=2;
    arr[2]=4;
    for(int i=3; i<11; i++){
        arr[i] = arr[i-1]+arr[i-2]+arr[i-3];
    }
    for(int i=0; i<cnt; i++){
        cin >> num;
        cout << arr[num-1] << '\n';
    }
    return 0;
}
