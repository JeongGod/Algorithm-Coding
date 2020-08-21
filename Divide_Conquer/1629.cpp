#include <cstdio>

long long mod;
long long multiple_dv(long long a, long long expo) {
    long long temp_ans;
    if(expo==1) return a%mod;
    else if(expo==0) return 1;
    else {
        if(expo%2 == 0) { // 짝수
            temp_ans = multiple_dv(a, expo/2);
            return (temp_ans*temp_ans)%mod;
        }
        else { // 홀수
            temp_ans = multiple_dv(a, (expo-1)/2);
            return ((temp_ans*temp_ans)%mod*a)%mod;
        }
    }
}

int main() {
    long long a,b;
    scanf("%lld %lld %lld", &a, &b, &mod);
    printf("%lld\n", multiple_dv(a,b));
}