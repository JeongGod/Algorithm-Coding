#include <iostream>
using namespace std;

void merge(int arr[], int left, int right, int mid){
    int i,j,k;
    int tmp_arr[right+1];
    i = left;
    j = mid+1;
    k = left;

    while(i<=mid && j<=right){
        if(arr[i] < arr[j]){
            tmp_arr[k] = arr[i];
            i++;
        }
        else {
            tmp_arr[k] = arr[j];
            j++;
        }
        k++;
    }
    if(i>mid){
        for(int m=j; m<=right; k++,m++) tmp_arr[k] = arr[m];
    }
    else{
        for(int m=i; m<=mid; k++,m++) tmp_arr[k] = arr[m];
    }

    for(int n=left; n<=right; n++) {
        arr[n] = tmp_arr[n];
    }
}

void merge_sort(int arr[], int left, int right) {
    int mid;
    if(left < right) {
        mid = (right+left)/2;

        merge_sort(arr,left,mid);
        merge_sort(arr,mid+1,right);

        merge(arr,left,right,mid);
    }
}

int main() {
    int cnt;
    cin >> cnt;
    int num[cnt];
    for(int i=0; i<cnt; i++) cin >> num[i];
    // mergesort
    merge_sort(num, 0, cnt-1);
    // End
    for(int i=0; i<cnt; i++) cout << num[i] << '\n';
    return 0;
}
