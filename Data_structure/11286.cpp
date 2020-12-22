#include <cstdio>
#include <stdlib.h>
/*
 * abs_min_Heap
 * 0 : pop
 * 0을 제외한 수 : in
 */
typedef struct Heap {
    int q[100002];
    int size;
} Heap;

void heap_in(Heap *heap,int tmp) {
    heap->size++;
    int i;
    for(i=heap->size; i>1; i/=2) {
        if(abs(heap->q[i/2]) > abs(tmp)) {
            heap->q[i] = heap->q[i/2];
        } else if(abs(heap->q[i/2]) == abs(tmp)) {
            if(tmp < heap->q[i/2]) {
                heap->q[i] = heap->q[i/2];    
            } else break;
        } else break;
    }
    heap->q[i] = tmp;
}
int heap_pop(Heap *heap) {
    int item = heap->q[1];
    int tmp = heap->q[heap->size--];
    int child, parent;
    child = 2; parent = 1;
    while(child <= heap->size) {
        if(abs(heap->q[child]) > abs(heap->q[child+1])) {
            child++;
        } else if(abs(heap->q[child]) == abs(heap->q[child+1])) {
            if(heap->q[child] > heap->q[child+1]) child++;
        }
        if(abs(tmp) > abs(heap->q[child])) {
            heap->q[parent] = heap->q[child];
            parent = child;
            child *= 2;
        } else if(abs(tmp) == abs(heap->q[child])) {
            if(tmp > heap->q[child]) {
                heap->q[parent] = heap->q[child];
                parent = child;
                child *= 2;
            } else break;
        } else break;
    }
    heap->q[parent] = tmp;
    return item;
}

int main(){
    int tc,n;
    Heap heap;
    heap.size=0;
    scanf("%d", &tc);
    for(int i=0; i<tc; i++) {
        scanf("%d", &n);
        if(n==0) {
            if(heap.size == 0) printf("0\n");
            else printf("%d\n", heap_pop(&heap));
        } else {
            heap_in(&heap, n);
        }
    }
    return 0;
}