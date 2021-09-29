# 수박수박수박수박 https://programmers.co.kr/learn/courses/30/lessons/12922

# 방법 1
def solution(n):
    answer = '수박'*(n//2+1)
    return answer[:n]

# 방법 2
def solution(n):
    s="수박"*n
    return s[:n]

# 방법 3
def solution(n):
    return ("수박"*n)[0:n]