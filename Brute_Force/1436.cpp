#include <iostream>
#include <cstdio>

int main(){
    int number[10001];
    int n,j=0,cnt=0;
    scanf("%d", &n);
    for(int i=666; i<10000000 && j<n; i++)
    {
        int num = i;
        while(true)
        {
            if(num%10 == 6) // 끝에자리가 6이라면
            {
                cnt++;  
                num /= 10;
            }
            else // 6이 아니라면
            {
                cnt = 0;
                num /= 10;
            }
            if(cnt >= 3) 
            {
                number[j++] = i; // 찾았다면 넣는다.
                break;
            }
            if(num == 0) break;
        }
        cnt = 0;
    }
    printf("%d\n", number[j-1]);
    return 0;
}
