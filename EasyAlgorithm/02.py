# 02 최대값 찾기

# ** 주어진 숫자 n개 중 가장 큰 숫자를 찾는 알고리즘을 만들어 보세요.

def find(a):
    n = len(a)
    max_n = a[0] # 리스트의 첫 번째 값을 최대값으로 기억함

    for i in range(1, n):
        if a[i] > max_n: # 이번 값이 기억된 최댓값보다 크면
            max_n = a[i] # 최대값을 다시 a[i] 로 변경
        return max_n



def find(a):
    n = len(a)
    max = a[0]
    for i in range(1,n):
        if a[i] > max:
            max = a[i]
        return max