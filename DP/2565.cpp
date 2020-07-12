#include <cstdio>
#include <string.h>
#include <algorithm>
using namespace std;
struct elec_line{ // 왼쪽을 기준으로 정렬시키기위해 구조체 사용.
    int left;
    int right;
};
int n;
struct elec_line *a;
void my_mergesort(int left, int right)
{
    int mid = (left+right)/2;
    int i = left;
    int j = mid+1;
    int k = left;
    elec_line *temp = new elec_line[n];
    while(i <= mid && j <= right)
    {
        if(a[i].left < a[j].left) temp[k++] = a[i++];
        else temp[k++] = a[j++];
    }
    while(i <= mid || j <= right)
    {
        if(i<=mid) temp[k++] = a[i++];
        else temp[k++] = a[j++];
    }
    for(int t=left; t<=right; t++) a[t] = temp[t];
    delete[] temp;
}

void my_partition(int left, int right)
{
    int mid;
    if(left < right)
    {
        mid = (left+right)/2;
        my_partition(left, mid);
        my_partition(mid+1,right);
        my_mergesort(left,right);
    }
}

int main()
{
    scanf("%d", &n);
    a = new elec_line[n];
    for(int i=0; i<n; i++) scanf("%d %d", &a[i].left, &a[i].right);
    my_partition(0,n-1); // 왼쪽을 기준으로 정렬한다.
    int num[102];
    int le,rig,ans=1;
    for(int i=0; i<n; i++) // 기준을 삼는다.
    {
        num[i] = 1;
        for(int j=0; j<i; j++) // 여기서 LIS알고리즘을 이용하여 최장 부분수열을 찾는다.
            if(a[i].right > a[j].right && num[i] <= num[j]) num[i]++;
        ans = max(ans, num[i]); 
    }
    delete[] a;
    printf("%d\n", n-ans);
    return 0;
}
/*
가장 최고의 시나리오는 왼쪽을 오름차순으로 정렬하였는데, 오른쪽도 오른차순으로 정렬이 되는 경우이다.
만약 오른쪽이 오름차순으로 가다가, 끊기는 경우가 생기면 거기가 바로 전깃줄이 겹치는 부분이다.
여기서 LIS알고리즘을 이용하여 최장증가수열을 구해, 전체 전깃줄에서 최장증가수열의 개수를 빼주면
그 개수는 곧 최장증가수열을 이루지 못하는 수열이므로 제외시키면 된다. 
*/