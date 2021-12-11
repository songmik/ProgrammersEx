# 01. 1부터 n까지의 합 구하기

# ** 1부터 n까지ㅣ 연속한 정수의 합을 구하는 알고리즘을 만들어 보세요.



# 방법 1 
def sum(n):
    s = 0 # 합을 계산할 변수 -> 초기화
    for i in range(1, n+1): # 1부터 n까지 반복할 거라 n+1까지 range를 정해줌
        s = s + i
    return s

# 방법 2
def sum(n):
    return n*(n+1) // 2 # // : 정수의 나눗셈
