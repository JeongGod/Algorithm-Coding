#include <cstdio>
int main()
{
    int n,ans=0;
    scanf("%d", &n);
    ans += n/5;
    ans += n/25;
    ans += n/125;
    printf("%d\n", ans);
    return 0;
}

/*
Trailing zero
5! => 1개
10! => 2개
15! => 3개
20! => 4개
25! => 6개
X! = 2**a * 5**b * m(임의의 수)로 이루어져 있는데 여기서
min(a,b)의 수가 곧 trailing zero의 개수가 된다.
무조건 b가 더 작게 나올 것이므로 b의 초점을 두면 되는데, 25는 5**2이므로
25의 배수에서는 2개씩 는다.
125의 배수에서는 3개씩 는다.
*/