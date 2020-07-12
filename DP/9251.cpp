#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;
int main()
{
    char a[1002];
    char b[1002];
    fgets(a,1002,stdin);
    fgets(b,1002,stdin);
    int a_len = strlen(a);
    int b_len = strlen(b);
    int ans[1003][1003];
    bool first;
    for(int i=0; i<a_len; i++) ans[i][0] = 0;
    for(int i=0; i<b_len; i++) ans[0][i] = 0;
    for(int i=0; i<a_len; i++) // 위에 (기준)
    {
        for(int j=0; j<b_len; j++) // 아래 (비교)
        {
            if(a[i] == b[j]) // 같은게 나오면
            {
                ans[i+1][j+1] = ans[i][j]+1; // 같다면 대각선(왼쪽)을 본다. 중복해서 나오면 안된다.
            }
            else // 다른게 나오면  
            {
            ans[i+1][j+1] = max(ans[i][j+1], ans[i+1][j]); // 다르다면 왼쪽과 위를 본다.
            }
        }
    }
    printf("%d\n", ans[a_len][b_len]-1); // -1은 fgets는 무조건 '\n'도 포함이 되어서 그걸 빼주는 것.
    return 0;
}

/*
LCS(Longest Common Subsequence)
기준 , 비교를 나눈다.
기준을 중심으로 비교해서 같다면 대각선(왼쪽)에서 +1, 다르다면 왼쪽과 위를 비교해 큰 값을 넣는다.
왜 대각선 왼쪽에서 +1을 하냐하면, 같다면은 비교하기 전 문자열의 길이에서 +1을 해야한다.
그런데 비교하기 전 문자열이라 함은 왼쪽 대각선이 맞다. 그냥 왼쪽은 이미 전 문자열과 비교를 한 상태이므로
중복해서 나오는 문자열같은 경우 에러가 난다.
다를때 왼쪽과 위를 비교하는 이유는, 어차피 다르기 때문에 비교를 해봤자 의미가 없다.
그렇다면 내가 알고 있는 길이 중 가장 큰 길이를 선정해야 하는데 그 길이가
바로 전에까지 비교했던 길이 or 전 문자가 비교했던 길이가 된다.
그래서 그 중에 가장 큰 길이를 선정한다.
*/