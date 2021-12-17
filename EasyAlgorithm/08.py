# 08. 삽입 정렬

# ** 리스트 안의 자료를 작은 수부터 큰 수 순서로 배열하는 정렬 알고리즘을 만들어 보세요.



# 방법 1. 쉽게 설명한 삽입 정렬 
def find(r, v): # 리스트 r에서 v가 들어갈 위치를 돌려주는 함수
    for i in range(0, len(r)): 
        if v < r[i]: # v값보다 i번 위치에 있는 자료 값이 크면 v가 그 값 바로 앞에 놓여야 정렬 순서가 유지됨
            return i
    return len(r) # 적절한 위치르르 못 찾았을 때는 리스트 맨 뒤에 삽입

def sort(a):
    result = []
    while a: # 리스트에 값이 남아 있는 동안 반복
        value = a.pop(0) # 리스트에서 맨 앞의 값을 꺼냄
        idx = find(result, value) # 꺼낸 값이 들어갈 위치를 찾기
        result.insert(idx, value) # 찾은 위치에 값 삽입 
    return result 


# 방법 2. 일반적인 삽입 정렬
def sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i] # i번 위치 값을 key에 저장
        j = i -1 # j를 i바로 왼쪽 위치에 저장
        while j >= 0 and a[j] > key: # 리스트의 j번 위치에 있는 값과 key를 비교해 key가 삽입될 적절한 위치를 찾음
            a[j+1] = a[j] # 삽입할 공간이 생기도록 값을 오른쪽으로 한 칸 이동
            j-=1
        a[j+1] = key # 찾은 삽입 위치에 key를 저장