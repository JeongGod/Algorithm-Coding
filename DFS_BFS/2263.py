import sys

input = sys.stdin.readline

sys.setrecursionlimit(1000000)

def bsearch(target):
    left, right = 0, len(bsearch_in)-1
    while left <= right:
        mid = (left + right) // 2
        if bsearch_in[mid][0] == target:
            return bsearch_in[mid][1]
        elif bsearch_in[mid][0] > target:
            right = mid
        else:
            left = mid+1

def search(pidx, start, end):
    global answer
    if start > end:
        return
    idx = bsearch(postorder[pidx])
    if not(start <= idx <= end):
        return
    
    
    # 부모에 대한 친구를 찾는다.
    answer.append(postorder[pidx])
    right = end - idx
    left = pidx - right
    search(left-1, start, idx-1)
    search(pidx-1, idx+1, end)


def solution(n : int, inorder : list[int], postorder : list[int]) -> list[int]:
    global answer
    answer = []

    # post-order을 거꾸로 가며 부모 정점을 찾는다.
    search(len(postorder)-1, 0, len(postorder)-1)

    return answer


if __name__ == "__main__":
    N = int(input())
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))
    bsearch_in = sorted([(val, idx) for idx, val in enumerate(inorder)])
    print(*solution(N, inorder, postorder))
"""
9
1 3 2 5 4 9 6 8 7
1 2 3 4 5 6 7 8 9
4
4 3 2 1
4 3 2 1
21
1 3 2 7 4 6 5 15 11 9 12 8 13 10 14 21 19 17 20 16 18
1 2 3 4 5 6 7 11 12 9 13 14 10 8 15 19 20 17 18 16 21
"""
