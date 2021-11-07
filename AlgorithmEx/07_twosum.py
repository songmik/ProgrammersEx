# 두 수의 합

# **덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

# 예제 입력 = nums =[2,7,11,15], target = 9 , 출력 [0,1]



# 방법 1. 브루트 포스로 계산 (브루트 포스 : 배열을 2번 반복하며 모든 조합을 더해서 일일이 확인해보는 무차별 대입 방식)
def solution(self, nums: List[str], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]


# 방법 2. in을 이용한 탐색 -> 모든 조합을 비교하지 않고 정답, 타겟에서 첫 번째 값을 뺀 값(target -n)이 존재하는지 탐색
def solution(self, nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement =  target - n

        if complement in nums[i+1:]:
            return [nums.index(n), nums[i+1:].index(complement) + (i+1)]


# 방법 3. 첫 번째 수를 뺀 결과 키 조회
def solution(self, nums: List[str], target: int) -> List[int]:
    # 키와 값을 바꿔서 딕셔너리로 저장
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


# 방법 4. 조회 구조 개선
def solution(self, nums: List[str], target: int) -> List[int]:
    nums_map = {}
    # 하나의 for 문으로 통합
    for i, num in enumerate(nums):
        if target -num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i
        

# 방법 5. 투 포인터 이용
def solution(self, nums: List[str], target: int) -> List[int]:
    left, right = 0, len(nums) -1
    while not left == right:
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로 (더해야 값이 커져서 오른쪽으로)
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로 (빼야 값이 작아져 왼쪽으로)
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]


