# 나누어 떨어지는 숫자 배열 https://programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer=[]
    for i in (arr):
        if i % divisor == 0 : # 나누어 떨어질 때
            answer.append(i) # 배열에 append해줌
    if len(answer) == 0: # 길이가 0이면 나누어 떨어질 수가 없어서
        answer.append(-1) # -1을 넣어줌
    else:
        answer.sort()
    return answer

# 한줄 풀이
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]

