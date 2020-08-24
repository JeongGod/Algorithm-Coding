#include <cstdio>
#define MOD 1000000007
long long multi(long long k, long long p) {
    long long ans = 1;
    while(p>0) {
        if(p%2 != 0) { // 홀수라면
            ans*=k;
            ans%=MOD;
        }
        k*=k;
        k%=MOD;
        p/=2;
    }
    return ans;
}

long long dv(long long n, long long k) {
    if(k==1) return n;
    else if(k==0) return 1;
    else {
        long long nam = MOD;
        long long k_nam = multi(k,nam-2);
        return ((((n%MOD)*(dv(n-1,k-1))%MOD)%MOD)*k_nam%MOD)%MOD;
    }
}

int main() {
    long long n,k;
    scanf("%lld %lld", &n, &k);
    printf("%lld\n", dv(n,k));
    return 0;
}

/*
외우는 방법!
n개중에서 k개를 뽑는 방법
k개중 1개를 이미 뽑았다면, n-1개중에서 k-1개를 뽑으면 된다.
k개중 1개를 먹지 않고 다른 걸 먹었다면 n-1개중에 k개를 먹으면 된다.
그 2가지를 더한 것이 n개중에서 k개를 뽑는 방법이다.
nCk = n-1Ck-1 + n-1Ck

이러한 방법을 이용하여
nCk = n-1Ck-1 + n-2Ck-1 + ... + k-1Ck-1

(a*b)%M = ((a%M)*(b%M))%M 성립.
(a/b)%M = ((a%M)/(b%M))%M 은 성립하지 않는다.
그래서 b를 나눗셈으로 보지 않고, 곱셈으로 바꾸기 위해 역원을 구한다.
(a*b**-1)%M = ((a%M)*(b**-1%M))%M은 성립한다.
하지만 b**-1%M의 값을 모른다. 그것을 구하기 위해 2가지 공식이 존재한다.

1. 유클리드 호제법
gcd(a,b) = ax+by
a,M이 서로소라는 가정하에
ax%M = 1 인 것을 찾는다면, x는 a에 대한 나머지 역원이다.
=> ax+My = gcd(a,M) = (ax+My) % M = gcd(a,M) % M
=> ax%M + My%M = gcd(a,M)%M
=> ax%M = gcd(a,M)%M
여기서 gcd(a,M)%M 이 1이라면, x는 a에대한 나머지 역원이다.

2. 페르마의 소정리
=> 1 = a**(p-1)%p
=> 1%p = a**(p-1)%p
양 변에 a**-1을 곱해주면
=> a**-1%p = a**(p-2)%p

*/