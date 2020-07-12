#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;
int main(){
    int n;
    int x1,y1,r1,x2,y2,r2;
    int dr,cnt,maxr,minr;
    double dxy;
    scanf("%d", &n);
    for(int i=0; i<n; i++){
        scanf("%d %d %d %d %d %d", &x1,&y1,&r1,&x2,&y2,&r2);
        cnt=0;
        dr = r1+r2;
        maxr = max(r1,r2);
        minr = min(r1,r2);
        dxy = sqrt(pow(x2-x1,2)+pow(y2-y1,2));
        if(r1==r2 && dxy==0){
            printf("-1\n");
        }
        else{
            if(maxr-dxy>minr){
                cnt=0;
            }
            else if(maxr-dxy==minr){
                cnt=1;
            }
            else{
                if(dxy>dr) cnt=0;
                else if(dxy==dr) cnt=1;
                else cnt=2;
            }
            printf("%d\n", cnt);
        }
    }
    return 0;
}
