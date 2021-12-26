# 포켓몬 https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    choose = int(len(nums)/2) # 주어지는 리스트는 짝수
    nums=set(nums) # nums에 있는 중복을 set으로 제거해줌
    answer = min(len(nums),choose)
    return answer

# set 함수 : 집합 함수로 순서가 없음
# 참고 : https://wikidocs.net/16044

# 간결한 코드
def solution(nums):
    return min(len(nums)/2, len(set(nums)))