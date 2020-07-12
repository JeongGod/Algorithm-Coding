#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

struct Point{
    int x;
    int y;
};

bool cmp(const Point &p1, const Point &p2){
    if(p1.w < p2.x){
        return true;
    }
    else if(p1.x == p2.x){
        return p1.y < p2.y;
    }
    else{
        return false;
    }
}

int main(){
    int n,k,max;
    int w[101] = {0,};
    int v[101] = {0,};
    double p[101] = {0,};
    scanf("%d %d", &n, &k);
    for(int i=0; i<n; i++){
        scanf("%d %d", &w[i], &v[i]);
        p[i] = double(v[i])/double(w[i]);
    }
    sort(p,p+n,cmp);
    for(int i=0; i<n; i++){
        // int temp = k;
        // if(temp>w[i]){
        //     max = v[i];
        //     temp -= w[i];
        //     for(int j=i+1; j<n; j++){
        //         if(temp>=w[j]){
        //             temp -= w[j];
        //             max += v[j];
        //         }
        //     }
        // }
        // else if(temp==w[i]) max = v[i];
        printf("%f\n", p[i]);
    }
    return 0;
}
