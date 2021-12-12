# 03. 동명이인 찾기 1

# ** n명의 사람 이름 중에서 같은 이름을 찾아 집합으로 만들어 돌려주는 알고리즘을 만들어보세요.



# 방법
def find_name(a):
    n = len(a)
    result = set() # 같은 이름을 저장할 빈 집합 생성 / set() : 빈 집합을 생성하는 함수
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] == a[j]: # i에서의 이름과 j에서의 이름이 같으면
                result.add(a[i]) # result에 이름을 add해줌
    return result


# 반복
def find(a):
    n = len(a) # 리스트의 자료 개수를 n에 저장
    result = set() 
    for i in range(0, n-1):
        for j in (i+1, n):
            if a[i] == a[j]:
                result.add(a[i])
    return result

    


