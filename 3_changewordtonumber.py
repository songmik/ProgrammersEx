# 숫자 문자열과 영단어 https://programmers.co.kr/learn/courses/30/lessons/81301


# 1. replace 이용
def solution(s):
    answer = ''
    dic={
        'zero':'0','one':'1','two':'2','three':'3','four':'4',
        'five':'5','six':'6','seven':'7','eight':'8','nine':'9' }
    answer = s
    for key, value in dic.items():
        answer = answer.replace(key,value)

    return int(answer)


# 2. isdigit 이용

def solution(s):
    answer=''
    dic={
        'zero':'0','one':'1','two':'2','three':'3','four':'4',
        'five':'5','six':'6','seven':'7','eight':'8','nine':'9' }
    num=''
    for word in s:
        if word.isdigit():
            answer += word
        else:
            num += word
            if num in dic.keys():
                answer+=dic[num]
                num=''
    return int(answer)
