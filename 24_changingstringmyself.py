# 문자열 내 마음대로 정렬하기 https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    answer=[]
    strings=sorted(strings)
    answer=sorted(strings, key=lambda x:x[n])
    return answer

# 짧은 코드
def solution(strings, n):
    return sorted(strings, key=lambda x:x[n])
