#include <iostream>
#include <cstdio>
#include <string.h>
using namespace std;

struct point
{
    int x;
    int y;
};

struct point *p;
int n;
void my_merge(int left, int right)
{
    int mid = (left+right) / 2;
    int i = left;
    int j = mid+1;
    int k = left;
    point *temp = new point[n];
    
    while(i <= mid && j <= right)
    {
        if(p[i].y < p[j].y) temp[k++] = p[i++];
        else if(p[i].y > p[j].y) temp[k++] = p[j++];
        else // x값이 같다면 y값 비교.
        {
            if(p[i].x <= p[j].x) temp[k++] = p[i++];
            else temp[k++] = p[j++];
        }
    }
    while(i <= mid || j <= right)
    {
        if(i<=mid) temp[k++] = p[i++];
        else temp[k++] = p[j++];
    }
    for(int i=left; i<=right; i++) p[i] = temp[i];
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
        my_merge(left,right);
    }
}

int main()
{
    scanf("%d\n", &n);
    p = new point[n];
    for(int i=0; i<n; i++) scanf("%d %d", &p[i].x , &p[i].y);
    // 좌표를 다 받는다.
    my_partition(0, n-1);
    for(int i=0; i<n; i++) printf("%d %d\n", p[i].x, p[i].y);
    // 좌표 출력문
    delete[] p;
    return 0;
}
