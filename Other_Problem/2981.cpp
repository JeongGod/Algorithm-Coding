#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <vector>
using namespace std;

vector<int> v;
int gcd(int num1, int num2) // 유클리드 호제법
{
    if(num1%num2 == 0) return num2;
    else
    {
        for(;;)
        {
            int temp = num2;
            num2 = num1%num2;
            num1 = temp;
            if(num1%num2 == 0) return num2;
        }
    }
}
int main()
{
    int n;
    int a[102];
    scanf("%d", &n);
    for(int i=0; i<n; i++) scanf("%d", &a[i]);
    // 오름차순 정렬
    sort(a, a+n);
    int great_cd = a[1]-a[0];
    for(int i=2; i<n; i++)
    {
        great_cd = gcd(great_cd, a[i]-a[i-1]);
    }
    for(int i=2; i*i<=great_cd; i++) // 약수찾기.
    {
        if(great_cd%i == 0)
        {
            v.push_back(i);
            v.push_back(great_cd/i);
        }
    }
    v.push_back(great_cd);
    // 오름차순 정렬
    sort(v.begin(), v.end());
    // 중복 제거
    v.erase(unique(v.begin(), v.end()), v.end());
    for(int i=0; i<v.size(); i++) printf("%d ", v[i]);
    printf("\n");
    return 0;
}
/*
a,b,c의 같은 나머지 r이라고 가정.
a>b>c라고 가정.
x = 임의의 수(다 같음), t = 몫(다름), r = 나머지(다 같음)
a = x(임의의 수)*t1 + r(나머지)
b = x*t2 + r
c = x*t3 + r

r로 정리해보면
a-b = x(t1-t2) 이런식으로 정리가 된다.
우리는 x를 알고 싶은것이기 때문에 x의 값들에 맞는 것을 찾기 위해선
a-b의 약수들이 곧 해가 된다.
여러개의 수가 들어왔다면 그 여러개의 수들에 대한 약수들의 교집합들이
답이다.
*/