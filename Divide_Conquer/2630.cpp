#include <cstdio>
int pan[129][129];
int blue_num=0, white_num=0;
bool first;
void divide(int start_x, int start_y, int end) {
    int chk = pan[start_x][start_y]; // 기준
    for(int i=start_x; i<start_x+end; i++) {
        for(int j=start_y; j<start_y+end; j++) {
            if(chk != pan[i][j]) {
                end /=2;
                divide(start_x, start_y, end); // 1구역 0,0 4,4
                divide(start_x+end, start_y, end); // 2구역 4,0 8,4
                divide(start_x, start_y+end, end); // 3구역 0,4 4,8
                divide(start_x+end, start_y+end, end); // 4구역 4,4 8,8
                return;
            }
            else continue;
        }
    }
    // continue로 다 같아.
    if(chk == 1) blue_num++;
    else white_num++;
}

int main() {
    int n;
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            scanf("%d", &pan[j][i]);
        }
    }
    // Divide
    divide(0, 0, n);
    printf("%d\n%d\n", white_num, blue_num);
    return 0;
}