#include <cstdio>
int pan[65][65];
int n;

void divide(int st_x, int st_y, int size) {
    int chk = pan[st_x][st_y];
    for(int i=st_x; i<st_x+size; i++) {
        for(int j=st_y; j<st_y+size; j++) {
            if(pan[i][j] != chk) { // 나누자
                size /= 2;
                printf("(");
                divide(st_x, st_y, size);
                divide(st_x+size, st_y, size);
                divide(st_x, st_y+size, size);
                divide(st_x+size, st_y+size, size);
                printf(")");
                return;
            } else continue;
        }
    }
    // 다 통과
    if(chk == 1) printf("1");
    else printf("0");
}

int main() {
    scanf("%d", &n);
    char temp[65][65];
    for(int i=0; i<n; i++) {
        scanf("%s", temp[i]);
    }
    for(int j=0; j<n; j++) {
        for(int i=0; i<n; i++) {
            pan[i][j] = temp[j][i]-'0';
        }
    }
    divide(0,0,n);
    printf("\n");
    return 0;
}