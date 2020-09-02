#include <cstdio>
#include <vector>
using namespace std;
vector<vector<char > > a(2189, vector<char>(2189, ' '));
void star(int n, int x, int y) {
    if(n==3) {
        for(int i=0; i<3; i++) {
            for(int j=0; j<3; j++) {
                if(i==1 && j==1) {
                    a[x+i][y+j] = ' ';
                }
                else a[x+i][y+j] = '*';
            }
        }
    } else {
        int temp = n/3;
        for(int i=0; i<3; i++) {
            for(int j=0; j<3; j++) {
                if(i==1 && j==1) continue;
                star(temp, x+i*temp, y+j*temp);
            }
        }
    }
}

int main() {
    int n;
    scanf("%d", &n);
    star(n,0,0);
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            printf("%c", a[i][j]);
        }
        printf("\n");
    }
    return 0;
}