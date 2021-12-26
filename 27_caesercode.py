# 시저 암호 https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])- ord('A') + n) % 26 + ord('A')) # 알파벳이 25글자라 더 큰 수인 26으로 나누어 줌
        elif s[i].islower():                                    # 맨 마지막이 다시 처음으로 돌아가는 경우를 방지
            s[i]=chr((ord(s[i])- ord('a') + n) % 26 + ord('a'))

    return "".join(s)

# ord : 문자의 유니코드 값을 돌려주는 함수로 chr() 과 반대 함수임.
# ord('a') = 97
# chr(97) = 'a'
# 참고 : https://wikidocs.net/32
