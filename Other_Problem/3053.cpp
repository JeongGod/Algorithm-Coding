#include <iostream>
#include <cstdio>
#include <cmath>
#define pi 3.14159265358979323846
int main(){
    int r;
    double taxi,cir;
    scanf("%d", &r);
    taxi = pow(2*r,2)/2;
    cir = pow(r,2)*pi;
    printf("%f\n%f\n", cir,taxi);
    return 0;
}
