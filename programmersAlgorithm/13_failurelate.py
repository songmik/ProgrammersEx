# 실패율 https://programmers.co.kr/learn/courses/30/lessons/42889

def solution (N, stages):
    dic = {} # 실패율을 구해 딕셔너리에 넣음
    num = len(stages)
    for i in range(1,N+1):
        if num != 0: # 0명이 되면 그 이후 스테이지는 0임
            count = stages.count(i) # 스테이지에 도달한 수를 셈
            dic[i]=count/num
            num -= count
        else:
            dic[i] = 0

    return sorted(dic, key=lambda x : dic[x],reverse = True )
    # sorted (정렬할 데이터, key 파라미터, reverse 파라미터(True=내림차순))
