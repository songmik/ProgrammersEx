# 10. 배열 파티션 1

# ** n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.

# 예제 : 입력 = [1,4,3,2], 출력 = 4
# 설명 : n은 2가 되며, 최대 합은 4이다. min(1,2) + min(3,4) = 4



# 방법 1. 오름차순 풀이
def solution(self, nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for i in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
        pair.append(i)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
    return sum


# 방법 2. 짝수 번째 값 계산
def solution(self, nums: List[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        # 짝수 번째 값의 합 계산
        if i % 2 == 0:
            sum += n
    return sum


# 방법 3. 파이썬다운 방식
def solution(self, nums: List[int]) -> int:
    return sum(sorted(nums)[::2])

