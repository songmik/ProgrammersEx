# 가운데 글자 가져오기 https://programmers.co.kr/learn/courses/30/lessons/12903

# 방법 1
def solution(s):
    answer = ''
    if len(s) % 2 == 1: # 홀수의 경우
        return s[int(len(s)/2)]
    else: # 짝수의 경우
        return s[int(len(s)/2)-1 : int(len(s)/2)+1]

# 방법 2 -> 방법 1 보다 더 간략한 풀이
def solution(s):
    return s[(len(s)-1)//2:len(s)//2+1]
