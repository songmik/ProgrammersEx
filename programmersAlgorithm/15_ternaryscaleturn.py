# 3진법 뒤집기 https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    answer=''

    while n > 0:
        n,i=divmod(n,3) # i를 3으로 나눈 몫과 나머지
        answer+=str(i)
    return int(answer,3)

# divmod(a,b) : 2개의 숫자를 입력받음, a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려줌
# 참고 : https://wikidocs.net/32#divmod

# int(x,base) : 숫자나 문자열 x로부터 만들어진 정수 객체를 돌려줌