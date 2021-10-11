# 소수만들기 https://programmers.co.kr/learn/courses/30/lessons/12977


# combinations : 중복을 허용하지 않고, 순서 의미가 있는 조합을 리턴해줌
# 참고 : https://wikidocs.net/106964
from itertools import combinations
# 수학적 계산을 하기위해 math 사용
# 참고 : https://wikidocs.net/75
import math

# 소수를 구하는 함수
def prime(n):

    # math.sqrt : 제곱근을 구해줌
    sqrt = math.sqrt(n)
    if sqrt < 2:
        return False # 제곱근이 2보다 작으면 소수가 아님 
    for i in range(2, int(sqrt+1)):
        if n % i == 0: # 나머지가 0이 나오면 소수가 아님 -> False
            return False
    return True # 나누어 떨어지지 않으면 소수

def solution(nums):
    answer = 0
    for num in combinations(nums, 3):
        if prime(sum(num)) == True:
            answer += 1
    return answer


# 소수 찾기 https://programmers.co.kr/learn/courses/30/lessons/12921

import math

def solution(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


