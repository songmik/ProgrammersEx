# 두 개 뽑아서 더하기 https://programmers.co.kr/learn/courses/30/lessons/68644

# list와 set이용
def solution(numbers):
    answer=[]
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
        return sorted(list(set(answer))) # 집합 자료형은 중복을 허용하지 않기 때문에 리스트를 집합 자료형으로 바꾸게 되면 중복이 모두 없어짐


# itertools import combination 이용
from itertools import combinations
def solution(numbers):
    answer=set()
    for i in list(combinations(numbers,2)): # numbers에 있는 숫자 중 2개를 뽑음
        answer.add(sum(i))
    return sorted(answer)

# itertools.combinations : 번호 몇 개 중 몇 개를 구할때 잘 씀
# 참고 : https://wikidocs.net/106964
# 사용법 : itertools.combinations(range(1,46),6) : 1~45에서 숫자 6개의 수를 뽑아 이터레이터로 리턴함

 