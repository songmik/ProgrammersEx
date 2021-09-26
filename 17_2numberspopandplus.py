# 두 개 뽑아서 더하기 https://programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations
def solution(numbers):
    answer=set()
    for i in list(combinations(numbers,2)):
        answer.add(sum(i))
    return sorted(answer)

# itertools.combinations : 번호 몇 개 중 몇 개를 구할때 잘 씀
# 참고 : https://wikidocs.net/106964
# 사용법 : itertools.combinations(range(1,46),6) : 1~45에서 숫자 6개의 수를 뽑아 이터레이터로 리턴함

 