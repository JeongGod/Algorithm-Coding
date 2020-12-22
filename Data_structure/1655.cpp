#include <cstdio>
#include <time.h>
#include <cmath>
#include <iostream>
using namespace std;

typedef struct Heap {
    int q[100002];
    int size;
} Heap;


void heap_in(int tmp, Heap *heap, int choice) {
    heap->size++;
    int i;
    for(i=heap->size; i>1; i/=2) 
    {
        if(choice) { // choice가 1이라는 것은 min_heap
            if(heap->q[i/2] > tmp) 
            {
                heap->q[i] = heap->q[i/2];
            } else break;
        } else { // max_heap
            if(heap->q[i/2] < tmp) 
            {
                heap->q[i] = heap->q[i/2];
            } else break;
        }
    }
    heap->q[i] = tmp;
}
int heap_pop(Heap *heap, int choice) {
    int item = heap->q[1];
    int tmp = heap->q[heap->size--];
    int child, parent;
    child = 2; parent = 1;
    while(child <= heap->size) 
    {
        if(choice)
        {
            if(heap->q[child] > heap->q[child+1]) child++;
            if(tmp > heap->q[child]) 
            {
                heap->q[parent] = heap->q[child];
                parent = child;
                child *= 2;
            } else break;
        }
        else
        {
            if(heap->q[child] < heap->q[child+1]) child++;
            if(tmp < heap->q[child]) 
            {
                heap->q[parent] = heap->q[child];
                parent = child;
                child *= 2;
            } else break;
        }
    }
    heap->q[parent] = tmp;
    return item;
}

int main() {
    int tc,n;
    scanf("%d", &tc);
    Heap max_heap;
    Heap min_heap;
    max_heap.size = 0;
    min_heap.size = 0;
    int middle = -10000;
    if(tc == 1) {
        scanf("%d", &n);
        printf("%d\n", n);
        return 0;
    } else if(tc == 2) {
        int a,b;
        scanf("%d %d", &a, &b);
        printf("%d\n", min(a,b));
        return 0;
    }
    for(int i=0; i<tc; i++) {
        // 중간값에 따라 max(왼쪽), min(오른쪽) 넣는다.
        printf("====================\n");
        printf("heap in : ");
        scanf("%d", &n);
        if(middle <= n) {
            heap_in(n, &min_heap, 1); // min
        } else {
            heap_in(n, &max_heap, 0); // max
        }

        if(max_heap.size - min_heap.size == 2)
        {
            heap_in(heap_pop(&max_heap, 0), &min_heap, 1);
        } else if(max_heap.size - min_heap.size == -2) {
            heap_in(heap_pop(&min_heap, 1), &max_heap, 0);
        }
        printf("out@@@@@@ : ");
        if(max_heap.size >= min_heap.size) 
            middle = max_heap.q[1];
        else 
            middle = min_heap.q[1];
        printf("%d\n", middle);

        printf("\nMax_Heap\n");
        for(int i=1; i<=max_heap.size; i++) {
            printf("%d ", max_heap.q[i]);
        }
        printf("\nMin_Heap\n");
        for(int i=1; i<=min_heap.size; i++) {
            printf("%d ", min_heap.q[i]);
        }
        printf("\n");
    }
}


// int main() {
    // int tc,n;
    // int dic[20002] = {0,};
    // int size = 0;
    // scanf("%d", &tc);
    // for(int i=0; i<tc; i++) {
    //     scanf("%d", &n);
    //     clock_t start = clock();
    //     dic[n+10000]++;
    //     size++;
    //     int tmp_size;
    //     if(size%2 == 0) tmp_size = size/2;
    //     else tmp_size = size/2 +1;
    //     // printf("size = %d\n", size);
    //     for(int i=0; i<=20000; i++) 
    //     {
    //         if(dic[i])
    //         {
    //             // printf("i = %d\n", i);
    //             // printf("tmp_size = %d\n", tmp_size);
    //             tmp_size -= dic[i];
    //         }
    //         if(tmp_size <= 0)
    //         {
    //             printf("%d\n", i-10000);
    //             break;
    //         }
    //     }
    //     clock_t end = clock();
    //     printf("Time: %lf\n", (double)(end - start)/CLOCKS_PER_SEC);
    // }
    // return 0;
// }