#include <cstdio>
#include <iostream>
#include <string.h>
using namespace std;

struct alpha
{
    char a[51];
    int len;
};
alpha *arr;
int n;
void my_mergesort(int left, int right)
{
    int same = 0;
    int mid = (left+right)/2;
    int i = left;
    int j = mid+1;
    int k = left;
    alpha *temp = new alpha[n];
    while(i <= mid && j <= right)
    {
        if(arr[i].len < arr[j].len) temp[k++] = arr[i++];
        else if(arr[i].len > arr[j].len) temp[k++] = arr[j++];
        else // 만약 길이가 같다면
        {
            if(strcmp(arr[i].a, arr[j].a) > 0) temp[k++] = arr[j++];
            else temp[k++] = arr[i++];
        }
    }

    while(i <= mid || j <= right)
    {
        if(i<=mid) temp[k++] = arr[i++];
        else temp[k++] = arr[j++];
    }
    for(int i=left; i<=right; i++) arr[i] = temp[i];
    delete[] temp;
}

void my_partition(int left, int right)
{
    int mid;
    if(left < right)
    {
        mid = (left+right)/2;
        my_partition(left, mid);
        my_partition(mid+1, right);
        my_mergesort(left, right);
    }
}

int main()
{
    scanf("%d", &n);
    arr = new alpha[n];
    for(int i=0; i<n; i++)
    {
        scanf("%s", arr[i].a);
        arr[i].len = strlen(arr[i].a);
    }
    my_partition(0,n-1);
    for(int i=0; i<n; i++) // 중복된 친구는 뺀다.
    {
        if(strcmp(arr[i].a, arr[i+1].a) == 0) continue;
        printf("%s\n", arr[i].a);
    }
    delete[] arr;
    return 0;
}