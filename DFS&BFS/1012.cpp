#include <cstdio>
#include <vector>
using namespace std;
vector<vector<int > > pan (52, vector<int> (52,0));
void check(int x, int y, int n) {
    if(x<0 || y<0 || x>n-1 || y>n-1 || pan[x][y] == 0) return;
    pan[x][y] = 0;
    check(x+1,y,n);
    check(x-1,y,n);
    check(x,y-1,n);
    check(x,y+1,n);
}

int main() {
    int tc;
    int temp_x,temp_y;
    scanf("%d", &tc);
    for(int i=0; i<tc; i++) {
        int m,n,num;
        int cnt = 0;
        scanf("%d %d %d", &m, &n, &num);
        for(int j=0; j<num; j++) {
            scanf("%d %d", &temp_x, &temp_y);
            pan[temp_x][temp_y] = 1;
        }
        for(int j=0; j<m; j++) {
            for(int k=0; k<n; k++) {
                if(pan[j][k] == 1) {
                    check(j,k,num);
                    cnt++;
                }
            }
        }
        printf("%d\n", cnt);
    }
    return 0;
}