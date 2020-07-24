#include <cstdio>
#include <stack>
using namespace std;
int main()
{
    int n,t,ans=0;
    stack<int> s;
    scanf("%d", &n);
    for(int i=0; i<n; i++)
    {
        scanf("%d", &t);
        if(t == 0) s.pop();
        else s.push(t);
    }
    while(!s.empty())
    {
        ans += s.top();
        s.pop();
    }
    printf("%d\n", ans);
    return 0;
}