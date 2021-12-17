# 09. 병합 정렬

# ** 리스트 안의 자료를 작은 수부터 큰 수 순서로 배열하는 정렬 알고리즘을 만들어 보세요.



# 방법 1. 쉽게 설명한 병합 정렬
def merge(a):
    n = len(a)
    if n <= 1: # 종료 조건 -> 리스트의 자료 개수가 한 개 이하이면 정렬할 필요 없음
        return a 
    mid = n // 2 # 중간을 기준으로 두 그룹으로 나눔
    g1 = merge(a[:mid]) # 첫 번째 그룹을 정렬 (앞부분)
    g2 = merge(a[mid:]) # 두 번째 그룹을 정렬 (뒷부분)
    result = [] 
    while g1 and g2: # 두 그룹에 자료가 남아있는 동안 반복
        if g1[0] < g2[0]: # 두 그룹의 맨 앞 자료 값을 비교
            result.append(g1.pop(0)) # g1이 작으면 값을 빼내어 결과 리스트에 추가
        else:
            result.append(g2.pop(0)) # g2가 작으면 값을 빼내어 결과 리스트에 추가
    
    # 아직 남아 있는 자료들을 결과에 추가 -> 빈 값은 while문을 바로 통과함
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result


# 방법 2. 일반적인 병합 정렬
def merge(a):
    n = len(a)
    if n <= 1: # 종료 조건
        return a
    mid = n // 2
    g1 = a[:mid]
    g2 = a[mid:]

    # 재귀 호출로 그룹을 정렬
    merge(g1) 
    merge(g2)

    # 두 그룹을 하나로 병합
    i1 = 0
    i2 = 0
    ia = 0
    while i1 <len(g1) and i2 <len(g2):
        if g1[i1] < g2[i2]:
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            a[ia] = g2[i2]
            i2 += 1
            ia += 1

    # 남아 잇는 자료들을 결과에 추가
    while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1
