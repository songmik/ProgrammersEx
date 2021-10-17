# 자연수 뒤집어 배열로 만들기 https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(s):
    natural = list(str(s)) 
    natural.reverse()
    return list(map(int, natural))


# 다른 풀이 1
def solution(s):
    return list(map(int, reversed(str(s))))

# 다른 풀이 2
def solution(s):
    return [int(i) for i in str(s)][::-1]