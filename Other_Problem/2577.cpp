#include <iostream>
#include <string>
using namespace std;

int main(){
    int a,b,c;
    int n0=0,n1=0,n2=0,n3=0,n4=0,n5=0,n6=0,n7=0,n8=0,n9=0;
    string ans;
    cin >> a >> b >> c;
    ans = to_string(a*b*c);

    for(int i=0; i<ans.length(); i++){
        switch (ans[i])
        {
            case '0':
                n0++;
                break;
            case '1':
                n1++;
                break;
            case '2':
                n2++;
                break;
            case '3':
                n3++;
                break;
            case '4':
                n4++;
                break;
            case '5':
                n5++;
                break;
            case '6':
                n6++;
                break;
            case '7':
                n7++;
                break;
            case '8':
                n8++;
                break;
            case '9':
                n9++;
                break;
        }
    }
    cout << n0 << '\n' << n1 << '\n' << n2 << '\n' << n3 << '\n' << n4 << '\n' << n5 << '\n' << n6 << '\n' << n7 << '\n' << n8 << '\n' << n9 << '\n';
    return 0;
}
