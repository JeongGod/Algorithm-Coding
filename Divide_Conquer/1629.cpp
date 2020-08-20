#include <cstdio>


int main() {
    long long int a,b,c;
    scanf("%lld %lld %lld", &a, &b, &c);
    printf("1 : %lld\n", a);
    for(int i=0; i<b; i++) {
        if(a>c) a %= c;
        else a *= a;
    }
    printf("2 : %lld\n", a);
    if(a>c) a %= c;
    printf("3 : %lld\n", a);
    return 0;
}


/*
(10 10 10 10 10 10)%4

10**6 => 10**3 10**3 => 10**2 * 10 * 10**2 * 10 => 10 10 10 10 10 10


7 3 5
7 7 7 => 
2 2 2 => 8
3 

7 3 9
7 7 7 
49%9 = 4
7*4 = 28 = 1


*/