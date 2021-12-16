# 07. 선택 정렬

# ** 주어진 리스트 안의 자료를 작은 수부터 큰 수 순서로 배열하는 정렬 알고리즘을 만들어보세요.



# 방법 1. 선택 정렬 
def find(a):
    n = len(a)
    min = 0
    for i in range(1, n):
        if a[i] < a[min]:
            min = i
    return min

def sort(a):
    result = [] # 새 리스트를 만들어 정렬된 값을 저장
    while a: # 주어진 리스트에 값이 계속 남아 있는 동안
        min = find(a) # 리스트에 남아 있는 값 중 최솟값의 위치
        value = a.pop(min) # 찾은 최솟값을 꺼내어 value에 저장
        result.append(value) # value를 result 리스트 끝에 추가
    return result


# 방법 2. 일반적인 선택 정렬 -> 주어진 리스트안에서 직접 자료의 위치를 바꾸면서 정렬시키는 프로그램
def sort(a):
    n = len(a)
    for i in range(0, n-1): # 0부터 n-2까지 반복
        # i번 위치부터 끝까지 자료 값 중 최솟값의 위치를 찾음
        min = i 
        for j in range(i+1, n):
            if a[j] < a[min]:
                min = j 
            a[i], a[min] = a[min] , a[i] # 찾은 최솟값을 i번의 위치로 변경