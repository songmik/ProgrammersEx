# 10. 이분 탐색

# ** 자료가 크기 순서대로 정렬된 리스트에서 특정한 값이 있는지 찾아 그 위치를 돌려주는 알고리즘을 만들어 보세요. 
# ** 리스트에 찾는 값이 없으면 -1을 돌려줍니다.



# 방법. 이분 탐색 알고리즘
def search(a,x): # a: 리스트, x: 찾는 값
    start = 0
    end = len(a) -1

    while start <= end: # 탐색할 범위가 남아 있는 동안 반복
        mid = (start + end) // 2 # 중간 위치
        if x == a[mid]: # 발견한다면
            return mid
        elif x > a[mid]: # 찾는 값이 더 크면 범위를 오른쪽으로 좁히며 계속 탐색
            start = mid + 1
        else:
            end = mid -1 # 찾는 값이 더 작으면 범위를 왼쪽으로 좁히며 계속 탐색

    return -1 # 찾는 값이 없을 때