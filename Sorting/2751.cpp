#include <iostream>
#include <cstdio>
using namespace std;

int a[1000001] = {0,};
int tmp_arr[1000001] = {0,};
void merge(int left, int mid, int right){
    int l = left;
    int m = mid+1;
    int i = left;
    while (l <= mid && m <= right){
        if(a[l]<a[m]){
            tmp_arr[i] = a[l];
            l++;
        }
        else{
            tmp_arr[i] = a[m];
            m++;
        }
        i++;
    }
    if(l>mid) for(;m <= right;m++,i++) tmp_arr[i] = a[m];
    else for(;l <= mid; l++, i++) tmp_arr[i] = a[l];
    for(int k=left; k<=right; k++) a[k] = tmp_arr[k];
}


void partition(int left, int right){
    if(left<right){
        int mid = (left+right)/2;
        partition(left, mid);
        partition(mid+1, right);
        merge(left, mid ,right);
    }
}

int main(){
    int n;
    scanf("%d", &n);
    for(int i=0; i<n; i++){
        scanf("%d", &a[i]);
    }
    partition(0, n-1);
    for(int i=0; i<n; i++){
        printf("%d ", a[i]);
    }
    printf("\n");
    return 0;
}



//
// void swap(int* a, int* b) {
//   int temp = *a;
//   *a = *b;
//   *b = temp;
// }
//
// int quick(int arr[] ,int low, int high){
//     int pivot = low;
//     int left = low+1;
//     while(left <= high){
//         while(arr[left]<arr[pivot]) left++;
//         while(arr[high]>arr[pivot]) high--;
//         if(left<high) swap(&arr[left],&arr[high]);
//     }
//     swap(&arr[high],&arr[pivot]);
//     return high;
// }
//
// void sort(int arr[], int left, int right){
//     if(left<right){
//         int pivot = quick(arr, left, right);
//         sort(arr,left,pivot-1);
//         sort(arr,pivot+1,right);
//     }
// }
//
// int main(){
//     int a[1000001] = {0,};
//     int n;
//     scanf("%d", &n);
//     for(int i=0; i<n; i++){
//         scanf("%d", &a[i]);
//     }
//     sort(a, 0, n-1);
//     for(int i=0; i<n; i++){
//         printf("%d ", a[i]);
//     }
//     printf("\n");
//     return 0;
// }
