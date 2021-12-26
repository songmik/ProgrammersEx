# 문자열 내 마음대로 정렬하기 https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    answer=[]
    strings=sorted(strings)
    answer=sorted(strings, key=lambda x:x[n])
    return answer

# 짧은 코드
def solution(strings, n):
    return sorted(strings, key=lambda x:x[n])

# 문자열 내림차순으로 배치하기 https://programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    return ''.join(sorted(s, reverse=True))

# 문자열 정렬 
# 1. sorted()
# sorted(<list>, key = <function>, reverse=<bool(True=내림차순, False=오름차순)>)

# 2. sort()
# <list>.sort(key=<funtion>, reverse=<bool>)