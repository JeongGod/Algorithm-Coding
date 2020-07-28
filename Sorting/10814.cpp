#include <cstdio>
#include <iostream>
#include <string.h>
struct member {
    int age;
    char name[101];
};
member *a;
int n;
void my_mergesort(int left, int right)
{
    int mid = (left+right)/2;
    int i = left;
    int j = mid+1;
    int k = left;
    member *temp = new member[n];
    while(i <= mid && j <= right)
    {
        if(a[i].age > a[j].age) temp[k++] = a[j++];
        else temp[k++] = a[i++];
    }
    while(i <= mid || j <= right)
    {
        if(i <= mid) temp[k++] = a[i++];
        else temp[k++] = a[j++];
    }
    for(int i=left; i<=right; i++) a[i] = temp[i];
    delete[] temp;
}

void my_partition(int left, int right)
{
    int mid;
    if(left < right)
    {
        mid = (left + right) /2;
        my_partition(left, mid);
        my_partition(mid+1, right);
        my_mergesort(left, right);
    }
}

int main()
{
    scanf("%d", &n);
    a = new member[n];
    for(int i=0; i<n; i++) scanf("%d %s", &a[i].age, a[i].name);
    my_partition(0, n-1);
    for(int i=0; i<n; i++) printf("%d %s\n", a[i].age, a[i].name);
    delete[] a;
    return 0;
}