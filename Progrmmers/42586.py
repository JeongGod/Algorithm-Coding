'''
List의 사이즈가 두 개 다 100이하로 작다는 것을 알고
완전탐색을 해도 상관없겠다 라는 생각과,
덱을 사용하지 않아도 되겠다는 생각이 들고 풀었습니다.
'''

def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0
        while True:
            for idx in range(len(progresses)):
                progresses[idx] += speeds[idx]
            if progresses[0] >= 100:
                break
        while progresses and progresses[0] >= 100:
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
            cnt += 1

        if cnt != 0:
            answer.append(cnt)
    return answer