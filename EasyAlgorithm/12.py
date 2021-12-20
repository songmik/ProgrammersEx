# 12. 동명이인 찾기2

# ** n명의 사람 이름 중에 같은 이름을 찾아 집합으로 만들어 돌려주는 알고리즘을 만들어보세요.



# 방법 -> 딕셔너리를 이용
def find(a):
    # 1단계 : 각 이름이 등장한 횟수를 딕셔너리로 만듦
    dic ={}
    for name in a:
        if name in dic: # 이름이 dic에 있으면
            dic[name] += 1 # 등장 횟수를 1증가
        else:
            dic[name] = 1 # 새 이름이면 등장 횟수를 1로 저장
            
    # 2단계 : 만들어진 딕셔너리에서 등장 횟수가 2 이상인 것을 결과에 추가
    result = set() # 결과값을 저장할 빈 집합
    for name in dic:
        if dic[name] >= 2:
            result.add(name)
    return result