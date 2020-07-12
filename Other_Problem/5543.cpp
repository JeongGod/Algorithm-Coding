#include <cstdio>
#include <iostream>

int main()
{
    int a,b,c,d,e;
    int sum_a, sum_b, sum_c;
    int result;
    scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);
    sum_a = (a+d > a+e) ? a+e : a+d;
    sum_b = (b+d > b+e) ? b+e : b+d;
    sum_c = (c+d > c+e) ? c+e : c+d;
    if(sum_a < sum_b && sum_a < sum_c) result = sum_a;
    else if(sum_b < sum_c && sum_b < sum_a) result = sum_b;
    else result = sum_c;
    printf("%d\n", result-50);
    return 0;
}