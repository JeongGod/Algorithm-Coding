import sys, heapq

input = sys.stdin.readline

def heappush(h: list, cur_index: int, val: int):
    """
    자식 노드는 현재 index * 2 (왼), index * 2 + 1 (오른)

    1. 맨 마지막에 append한다.
    2. 부모 노드와 비교한다. 만약 최상위 노드라면 끝
    3. 부모 노드보다 작다면
        - 부모 노드를 내리고 올라간다
    4. 부모 노드보다 크다면
        - 그대로 끝
    """
    parent_index = cur_index // 2
    # 최상위 노드
    if parent_index == 0 or h[parent_index] <= val:
        h[parent_index] = val
        return
    
    if h[parent_index] > val:
        h[cur_index] = h[parent_index]
        heappush(h, parent_index, val)

def heappop(h: list):
    """
    1. 첫번째 노드를 pop한다.
    2. 자식 노드중 작은 노드를 찾는다.
    3. 작은 노드가 부모 노드를 replace한다
    4. 리프노드까지 반복
    """
    cur_index = 1
    ans = h[cur_index]
    while True:
        left, right = cur_index * 2, (cur_index * 2) + 1
        if h[right] == 0 or h[left] < h[right]:
            h[cur_index] = h[left]
            cur_index = left
        else:
            h[cur_index] = h[right]
            h[right] = 0
            cur_index = right
    return ans

class Heap():
    h = []

    def push(self, val):
        self.h.append(val)
        self._push(len(self.h) - 1, val)

    def _push(self, index, val):
        # 스왑
        if index == 0 or self.h[(index - 1) // 2] <= val:
            self.h[index] = val
            return
        self.h[index] = self.h[(index - 1) // 2]
        self._push((index - 1) // 2, val)

    def pop(self):
        self.h[0], self.h[-1] = self.h[-1], self.h[0]
        ans = self.h.pop()
        self._heapify(0)
        return ans

    def _heapify(self, index):
        left, right = index * 2 + 1, (index * 2) + 2
        # leaf 노드 체크
        if left > len(self.h) - 1 and right > len(self.h) - 1:
            return
        elif left == len(self.h) - 1 and right > len(self.h) - 1:
            right = left

        if self.h[left] <= self.h[right]:
            self.h[index], self.h[left] = self.h[left], self.h[index]
            self._heapify(left)
        else:
            self.h[index] ,self.h[right] = self.h[right], self.h[index]
            self._heapify(right)
"""
1. x, y 를 고른다 (index는 같지 않음)
2. x+y 를 덮어씌운다. x+y, x+y
3. m번 반복한다.
4. 그 값들의 합이 최소가 만들게 한다.
"""
if __name__ == "__main__":
    N, M = map(int, input().split())

    CARDS = [*map(int, input().split())]
    hq = Heap()
    for i in range(N):
        hq.push(CARDS[i])

    for _ in range(M):
        x, y = hq.pop(), hq.pop()
        hq.push(x+y)
        hq.push(x+y)
        print(hq.h)
    print(sum(hq.h))
    # heapq.heapify(CARDS)
    # for _ in range(M):
    #     x = heapq.heappop(CARDS)
    #     y = heapq.heappop(CARDS)

    #     heapq.heappush(CARDS, x+y)
    #     heapq.heappush(CARDS, x+y)
    # print(sum(CARDS))