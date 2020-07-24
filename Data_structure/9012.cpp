#include <cstdio>
#include <stack>
#include <cstring>
using namespace std;
bool pair_check(char t[])
{
    stack<char> s;
    for(int j=0; j<strlen(t); j++)
    {
        if(t[j] == '(') s.push(t[j]);
        else
        {
            if(!s.empty()) s.pop();
            else
            {
               return false;
            }
        }
    }
    if(s.empty()) return true;
    else return false;
}

int main()
{
    int tc;
    char t[51];
    scanf("%d", &tc);
    for(int i=0; i<tc; i++)
    {
        scanf("%s", t);
        if(pair_check(t)) printf("YES\n");
        else printf("NO\n");
    }   
    return 0;
}