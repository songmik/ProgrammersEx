# 두 정수 사이의 합 https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a,b):
    if a < b:
        return sum(list(range(a,b+1)))
    else:
        return sum(list(range(b, a+1)))

# 다른 풀이
def solution(a,b):
    return (abs(a-b)+1)*(a+b)//2

# abs 함수 : 떤 숫자를 입력받았을 때, 그 숫자의 절댓값을 돌려주는 함수

