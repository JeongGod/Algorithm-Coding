#include <cstdio>
#include <cstring>
#include <stack>
using namespace std;
bool pair_check(char t[])
{
    stack<char> s;
    for(int j=0; j<strlen(t)-1; j++)
    {
        if(t[j] == '(' || t[j] == '[') s.push(t[j]);
        else if(t[j] == ')' || t[j] == ']')
        {
            if(!s.empty())
            {
                if(s.top() != '(' && t[j] == ')') return false;
                else if(s.top() != '[' && t[j] == ']') return false;
                else s.pop();
            }
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
    char t[120];
    for(;;)
    {
        fgets(t, 120, stdin);
        if(t[0] == '.') break;
        if(pair_check(t)) printf("yes\n");
        else printf("no\n");

    }
    return 0;
}