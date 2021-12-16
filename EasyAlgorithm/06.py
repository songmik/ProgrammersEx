# 06. 순차 탐색

# ** 주어진 리스트에 특정한 값이 있는지 찾아 그 위치를 돌려주는 알고리즘을 만들어 보세요. 
# ** 리스트에 찾는 값이 없다면 -1을 돌려줍니다.



# 방법 -> 순차 탐색 : 리스트 안에 있는 원소를 하나씩 순차적으로 비교하면서 탐색한다.
# 해당 값을 찾으면 그 값의 위치를 돌려주고, 찾지 못하면 -1을 돌려줌
def search(a,x): # a: 리스트 , x: 찾는 값 
    n = len(a) 
    for i in range(0, n):
        if x == a[i]: # 찾는 값이 a[i]와 같다면 
            return i # 위치를 돌려줌

    return -1 # 끝까지 비교해도 없으면 -1을 돌려줌


# 반복
def search(a,x):
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            return i 
    return -1

    