#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main(){
    int a,n;
    char word[21];
    string p;
    scanf("%d", &a);
    for(int i=0; i<a; i++){
        scanf("%d %s", &n, word);
        p = word;
        for(int j=0; j<strlen(word); j++){
            for(int k=0; k<n; k++){
                printf("%c", word[j]);
            }
        }
        printf("\n");
    }
    return 0;
}
