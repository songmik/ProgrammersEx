# 13. 친구의 친구 찾기

# ** 친구 관계를 이용하여 어떤 한 사람이 직접 또는 간접으로 아는 모든 친구를 출력하는 알고리즘을 만들어 보세요.



# 방법 
def friends(g, start): # g : 친구 관계 그래프 , start : 모든 친구를 찾을 자기 자신
    q = [] # 앞으로 처리해야 할 사람들을 큐에 저장
    done = set() # 이미 큐에 추가한 사람들을 집합에 기록

    q.append(start) # 자기 자신을 큐에 넣고 시작
    done.add(start) # 집합에도 추가

    while q:
        p = q.pop(0) 
        print(p)
        for x in g[p]: # 친구들 중에
            if x not in done: # 아직 큐에 추가된 적이 없는 사람을
                q.append(x) # 큐에 추가
                done.add(x) # 집합에 추가
