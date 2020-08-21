#include <cstdio>
int pan[2200][2200];
int n, minus=0, zero=0, plus=0;
void divide(int st_x, int st_y, int size) {
    int chk = pan[st_x][st_y];
    for(int i=st_x; i<st_x+size; i++) {
        for(int j=st_y; j<st_y+size; j++) {
            if(chk != pan[i][j]) {
                size /= 3;
                divide(st_x,st_y,size); // 1
                divide(st_x,st_y+size,size);
                divide(st_x,st_y+(2*size),size);
                divide(st_x+size,st_y,size); // 1
                divide(st_x+size,st_y+size,size);
                divide(st_x+size,st_y+(2*size),size);
                divide(st_x+(2*size),st_y,size); // 1
                divide(st_x+(2*size),st_y+size,size);
                divide(st_x+(2*size),st_y+(2*size),size);
                return;
            }
        }
    }
    if(chk == -1) minus++;
    else if(chk == 0) zero++;
    else plus++;
    return;
}

int main() {
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            scanf("%d", &pan[j][i]);
        }
    }

    divide(0,0,n);
    printf("%d\n%d\n%d\n", minus, zero, plus);
    return 0;
}