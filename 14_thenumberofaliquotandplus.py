# 약수의 개수와 덧셈 https://programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    answer=0
    for i in range(left, right+1): # left부터 right까지 1씩 증가
        count=0 # 약수의 개수를 담는 변수
        for j in range(1, i+1): # 1~i까지 약수를 찾음
            if i % j ==0: # 나누어 떨어지는 수는 약수임
                count+=1
        
        if count %2 ==0: # 개수가 홀수인지 짝수인지 판별
            answer+=i # 짝수면 더해줌
        else:
            answer-=i
    return answer



# 더 짧은 코드
def solution(left, right):
    answer=0
    for i in range(left, right+1):
        if int(i**0.5)==i**0.5: # 약수의 개수가 홀수인 제곱수를 판별
            answer -=i # 제곱수일 경우 빼줌
        else:
            answer+=i
    return answer
