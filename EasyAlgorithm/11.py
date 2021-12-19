# 11. 회문 찾기(큐와 스택) -> 순서대로 읽어도 거꾸로 읽어도 같은 낱말이나 문장 (= palindrome)

# ** 문자열이 회문인지 아닌지 판단하여 회문이면 True, 아니면 False를 결과로 알려주는 알고리즘을 만들어 보세요.



# 방법
def palindrome(s):
    q=[] # 큐
    s=[] # 스택

    # 1단계 : 문자열의 알파벳 문자를 각각 큐와 스택에 넣음
    for i in s:
        if i.isalpha(): # 해당 문자가 알파벳이면 , 큐와 스택에 그 문자를 추가
            q.append(i.lower())
            s.append(i.lower())

    # 2단계 : 큐와 스택에 들어 있는 문자를 꺼내면서 비교
    while q: # 큐에 문자가 남아있는 동안 비교
        if q.pop(0) != s.pop(0): # 큐와 스택에서 꺼낸 문자가 다르면 회문이 아니다
            return False
    return True



