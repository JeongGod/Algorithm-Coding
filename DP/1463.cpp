#include <iostream>
using namespace std;

int haha(int b){
    int a[b];
    for(int i=0; i<b; i++){
        a[0] = 0;
        a[1] = 1;
        a[2] = 1;
        if(i>2){
            if((i+1)%3 == 0) a[i] = min(1+a[i/3],1+a[i-1]);
            else if ((i+1)%2 == 0) a[i] = min(1+a[i/2],1+a[i-1]);
            else a[i] = 1+a[i-1];
        }
    }
    return a[b-1];
}

int main() {
    int n;
    cin >> n;
    cout << haha(n) << '\n';
    return 0;
}
