#include <cstdio>
#include <cstdlib>
#include <cmath>
int main()
{
    char exp[51];
    int num[51] = {0,};
    int start=0;
    int n,j=0,k=0;
    int ans=0;
    // 입력 받기.
    for(n=0; n<51; n++)
    {
        scanf("%c", &exp[n]);
        if(exp[n] == '\n') break;
    }
    // 숫자는 숫자로 다 변환
    for(int i=n-1; i>=0; i--)
    {
        if(exp[i] != '+' && exp[i] != '-') // 숫자라면
        {
            num[k] += pow(10,j++) * (exp[i]-'0');
        }
        else k++,j=0; // 숫자가 아니라면
    }
    // 계산하기
    ans = num[k];
    start=k-1;
    for(int i=0; i<n; i++)
    {
        if(exp[i] == '-') break; // -를 만났다면 뒤에있는 수는 다 빼면 되므로 break
        else if(exp[i] == '+')// +라면
        {
            ans += num[start--];
        }
    }
    for(;start>=0;) ans -= num[start--]; // - 계산
    printf("%d\n", ans);
    return 0;
}