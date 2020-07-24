#include <cstdio>
#include <iostream>
#include <string>
#include <map>
using namespace std;
int main()
{
    int tc,n;
    string clothes;
    scanf("%d", &tc);
    for(int i=0; i<tc; i++)
    {
        int ans = 1;
        map<string,int> m;
        scanf("%d ", &n); // 띄어쓰기 하나로 엔터를 문자로 들어가지 않게끔 만든다.
        for(int j=0; j<n; j++)
        {
            getline(cin, clothes);
            int p = clothes.find(' ');
            string kind = clothes.substr(p+1);
            m[kind]++;
        }
        map<string,int>::iterator iter;
        for(iter = m.begin(); iter != m.end(); iter++)
            ans *= (iter->second +1); // string, int중 2번째 인자인 int를 가져온다.
        printf("%d\n", ans-1);
    }
    return 0;
}