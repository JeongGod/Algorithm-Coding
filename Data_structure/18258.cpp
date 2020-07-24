#include <cstdio>
#include <iostream>
#include <cstring>
#include <queue>
using namespace std;
int main()
{
    int n,m;
    char cmd[10];
    queue<int> q;
    scanf("%d ", &n);
    for(int i=0; i<n; i++)
    {
        scanf("%s", cmd);
        if(strcmp(cmd, "push") == 0)
        {
            scanf("%d", &m);
            q.push(m);
        }
        else if(strcmp(cmd, "pop") == 0)
        {
            if(q.empty()) printf("-1\n");
            else
            {
                printf("%d\n", q.front());
                q.pop();
            }
        }
        else if(strcmp(cmd, "size") == 0)
        {
            printf("%lu\n", q.size());
        }
        else if(strcmp(cmd, "empty") == 0)
        {
            if(q.empty()) printf("1\n");
            else printf("0\n");
        }
        else if(strcmp(cmd, "front") == 0)
        {
            if(q.empty()) printf("-1\n");
            else printf("%d\n", q.front());
        }
        else if(strcmp(cmd, "back") == 0)
        {
            if(q.empty()) printf("-1\n");
            else printf("%d\n", q.back());
        }
    }
    return 0;
}