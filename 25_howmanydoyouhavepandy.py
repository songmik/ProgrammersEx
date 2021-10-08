# 문자열 내 p와 y의 개수 https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    answer=True
    x=s.count('p')+s.count('P')
    y=s.count('y')+s.count('Y')

    if x==y:
        return True
    else:
        return False

# 짧은 코드
def solution(s):
    return s.lower().count('p')==s.lower().count('y')

# lower() : 대문자를 소문자로 바꾸는 함수 (upper() : 소문자 -> 대문자)



