# 문자열 압축 https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    length = []
    result =''

    if len(s) == 1: # input된 문자열의 길이가 1이라면 1을 return해줌
        return 1
    for i in range(1, len(s)//2 + 1): # 자를 길이의 반복문
        count = 1 # count=1 로 초기화 해 줌.
        tmp = s[:i] 
        for j in range(i, len(s), i): 
            if s[j:j+i] == tmp: 
                count += 1
            else:
                if count == 1:
                    count =''
                result += str(count) + tmp
                tmp = s[j:j+i]
                count =1
        if count ==1:
            count =''
        result += str(count) + tmp
        length.append(len(result))
        result=''

    return min(length)

