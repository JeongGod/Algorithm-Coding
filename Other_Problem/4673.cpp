#include <iostream>
using namespace std;

int arr[10001] = {0,};

void self(int n){
    int sum=n, nam;
    while(true){
        if(n==0) break;
        nam = n%10;
        n /= 10;
        sum += nam;
    }
    for(int i=0; i<10000; i++){
        if(sum == i+1) arr[i] = 1;
    }
}

int main(){
    for(int i=1; i<=10000; i++){
        self(i);
    }
    for(int i=1; i<=10000; i++){
        if(arr[i-1]==0) cout << i << '\n';
    }
    return 0;
}
