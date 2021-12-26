# 음양 더하기 https://programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    answer = 0
    for num, sign in zip(absolutes, signs):
        if sign == True: # 참인 경우 양수이므로 더해줌
            answer += num
        elif sign == False: # 거짓인 경우 음수이므로 빼줌
            answer -= num
    return answer

# zip 함수 : 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수
# (참고 : https://wikidocs.net/32#zip)