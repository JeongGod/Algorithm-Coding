#include <cstdio>
#include <stack>
#include <cstring>
using namespace std;
int main()
{
    int n,k,j;
    int a[100003];
    char ans[200006];
    stack<int> s;
    scanf("%d", &n);
    for(int i=0; i<n; i++) scanf("%d", &a[i]);
    k = 0,j = 0; // a's index
    s.push(1);
    ans[j++] = '+';
    for(int i=2; k<n && i<=n+1;)
    {
        if(!s.empty())
        {
            if(s.top() == a[k])
            {
                s.pop();
                k++;
                ans[j++] = '-';
            }
            else
            {
                s.push(i++);
                ans[j++] = '+';
            }
        }
        else 
        {
            s.push(i++);
            ans[j++] = '+';
        }
    }
    int len = strlen(ans);
    if(k==n) 
    {
        for(int i=0; i<len; i++) printf("%c\n", ans[i]);
    }
    else printf("NO\n");
    return 0;
}

/*
1. 수열을 받는다.
2. 일단 작은 숫자부터 넣는다.(무조건)

*/