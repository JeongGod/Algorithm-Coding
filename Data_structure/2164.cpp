#include <cstdio>
#include <queue>
using namespace std;
int main()
{
    int n;
    queue<int> q;
    scanf("%d", &n);
    for(int i=1; i<=n; i++) q.push(i);
    for(;;)
    {
        if(q.size() == 1) break;
        q.pop();
        if(q.size() == 1) break;
        q.push(q.front());
        q.pop();
    }
    printf("%d\n", q.front());
    return 0;
}