# 완주하지 못한 선수 https://programmers.co.kr/learn/courses/30/lessons/42576

# 가장 좋아요가 많은 풀이
# collections : 파이썬 내장 컨테이너 (dict,list,set,tuplt) 에 대한 대안을 제공하는 특수 컨테이너 데이터형을 구현
# Counter : 데이터의 개수를 효과적으로 셀 수 있게 함
# 참고 : https://docs.python.org/ko/3/library/collections.html#module-collections

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion) # 겹치는 요소를 빼줌 (객체끼리 뺄셈이 가능함)
    return list(answer.keys())[0] # list [0]이 완주하지 못한 선수의 이름이 됌

