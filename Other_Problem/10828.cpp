#include <iostream>
#include <string>

using namespace std;
int k = 0;
int stack[10001];

void push(int num){
    stack[k] = num;
    k++;
}
void pop(){
    if(k>0){
        k--;
        cout << stack[k] << '\n';
        stack[k] = '\0';
    }
    else cout << "-1" << '\n';
}

int empty(){
    if(k>0) return 0;
    else return 1;
}
int top(){
    if(k>0) return stack[k-1];
    else return -1;
}

int main(){
    string command[] = {"push", "pop", "size", "empty", "top"};
    string insert;
    int cnt, num;
    cin >> cnt;
    for(int i=0; i<cnt; i++){
        cin >> insert;

        if(insert.find("push") != string::npos) {
            cin >> num;
            push(num);
        }
        else if(insert.find("pop") != string::npos) {
            pop();
        }
        else if(insert.find("size") != string::npos) {
            cout << k << '\n';
        }
        else if(insert.find("empty") != string::npos) {
            cout << empty() << '\n';
        }
        else if(insert.find("top") != string::npos) {
            cout << top() << '\n';
        }
    }
    return 0;
}
