#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main(){
    int len,cnt=0;
    char a[101];
    scanf("%s", a);
    len = strlen(a);
    for(int i=0; i<len; i++){
        if(a[i] == 'c' && a[i+1] == '='){
            i++;
            cnt++;
        }
        else if(a[i] == 'c' && a[i+1] == '-'){
            i++;
            cnt++;
        }
        else if(a[i] == 'd' && a[i+1] == 'z' && a[i+2] == '='){
            i+=2;
            cnt++;
        }
        else if(a[i] == 'd' && a[i+1] == '-'){
            i++;
            cnt++;
        }
        else if(a[i] == 'l' && a[i+1] == 'j'){
            i++;
            cnt++;
        }
        else if(a[i] == 'n' && a[i+1] == 'j'){
            i++;
            cnt++;
        }
        else if(a[i] == 's' && a[i+1] == '='){
            i++;
            cnt++;
        }
        else if(a[i] == 'z' && a[i+1] == '='){
            i++;
            cnt++;
        }
        else{
            cnt++;
        }
    }
    // c- dz= d- lj nj s= z=
    printf("%d\n", cnt);
    return 0;
}
