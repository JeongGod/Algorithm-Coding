#include <cstdio>

/*
 * Min_Heap
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
        if(heap->q[i/2] > tmp) {
            heap->q[i] = heap->q[i/2];
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
        if(heap->q[child] > heap->q[child+1]) child++;
        if(tmp > heap->q[child]) {
            heap->q[parent] = heap->q[child];
            parent = child;
            child *= 2;
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