#include <cstdio>

int main() {
    int n, temp;
    scanf("%d", &n);
    if(n%2) temp = n/2+1;
    else temp = n/2;
    for(int i=0; i<n; i++) {
        for(int j=0; j<temp; j++) {
            printf("* ");
        }
        printf("\n ");
        for(int j=temp; j<n; j++) {
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}