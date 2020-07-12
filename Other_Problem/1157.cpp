#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;
int main(){
    int n;
    int len,cnt,max=0;
    char a[1000001];
    int b[1000001] = {0,};
    char alpha;
    scanf("%s", a);
    len = strlen(a);
    for(int i=0; i<len; i++) a[i] = toupper(a[i]); //대문자로 통일
    for(int k=0; k<len; k++){
        cnt=0;
        if(b[k]==0){
            for(int j=k; j<len; j++){
                if(a[k] == a[j]) {
                    b[j]=1;
                    cnt++;
                }
            }
        }
        if(cnt>max){
            max=cnt;
            alpha = a[k];
        }
        else if(cnt==max){
            alpha = '?';
        }
    }
    printf("%c\n", alpha);
    return 0;
}
