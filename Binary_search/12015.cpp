#include <cstdio>
int a[1000003];
int lis[1000003];

void binary_search(int num, int len) {
    int left = 0;
    int right = len;
    int mid;
    while(left <= right) {
        mid = (left+right)/2;
        if(lis[mid] > num) {
            right = mid-1;
        } else if(lis[mid] < num) {
            left = mid+1;
        } else {
            left = mid;
            break;
        }
    }
    printf("left = %d, mid = %d, right = %d\n", left, mid, right);
    
    lis[left] = num;
}

int main() {
    int n;
    scanf("%d", &n);
    for(int i=0; i<n; i++) scanf("%d", &a[i]);
    lis[0] = a[0];
    int size = 0;
    for(int i=1; i<n; i++) {
        if(a[i] > lis[size]) {
            printf("if문=========\n");
            printf("a = %d\n", a[i]);
            printf("lis = %d\n", lis[size]);
            printf("size = %d\n", size);
            size++;
            lis[size] = a[i];
        } else {
            printf("else문=========\n");
            printf("a = %d\n", a[i]);
            printf("lis = %d\n", lis[size]);
            printf("size = %d\n", size);
            binary_search(a[i], size);
        }
        printf("---------lis--------\n");
        for(int i=0; i<=size; i++) printf("%d ", lis[i]);
        printf("\n");
    }
    for(int i=0; i<=size; i++) printf("%d ", lis[i]);
    printf("\n");
    printf("%d\n", size+1);
    return 0;
}