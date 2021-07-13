def solution(phone_book):
    '''
    도저히 감이 잡히지 않아 구글링을 했습니다..
    파이썬에서의 sort는 문자열도 해주는데 문자열의 값 -> 문자열의 길이 순으로
    정렬해준다는 것을 알았습니다.
    ex) ["119", "999393", "191", "121"] => ["119", "121", "191", "999393"]
    그래서 이런 식으로 코드를 짜도 가능합니다.    
    '''
    # phone_book.sort()
    # for idx in range(len(phone_book)-1):
    #     if phone_book[idx+1].startswith(phone_book[idx]):
    #         return False

    # 해쉬에 대한 맞는 풀이
    _dict = set()
    for num in phone_book:
        _dict.add(num)
    
    for num in phone_book:
        tmp = ""
        for idx in num:
            tmp += idx
            if tmp in _dict and tmp != num:
                return False
    
    return True