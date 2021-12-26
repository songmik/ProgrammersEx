# 이상한 문자 만들기 https://programmers.co.kr/learn/courses/30/lessons/12930?language=python3

def solution(s):
    answer=[]
    s = s.split(' ')
    for i in range(len(s)):
        result= ''
        for j in range(len(s[i])):
            if j % 2 == 0:
                result += s[i][j].upper()
            else:
                result += s[i][j].lower()
        answer.append(result)
    return ' '.join(answer)



# 간단한 풀이

def solution(s):
    return ' '.join(map(lambda x: ''.join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(' ')))

# enumerate : 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 때 사용
#             인덱스 번호와 컬렉션의 운소를 tuple 형태로 반환함
# 참고 : https://wikidocs.net/16045