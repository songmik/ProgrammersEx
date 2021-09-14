# k번째수 https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for command in commands: # commands에 있는 command i, j, k를 뽑음
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer

# sorted : 파이썬 내장 함수 
# 첫 번째 매개변수로 들어온 데이터를 새롭게 정렬된 리스트로 만들어 반환해줌


# 가장 좋아요가 많은 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# lambda : 함수를 한 줄로 만들어주는 함수 ( 사용법 -> lambda 인자 : 표현식 )
# 참고 https://wikidocs.net/64 