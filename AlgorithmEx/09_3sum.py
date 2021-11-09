# 9. 세 수의 합(★★)

# ** 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.

# 예제 입력 : nums = [-1,0,1,2,-1,-4] , 
#      출력 : [
#              [-1,0,1],
#              [-1,-1,2]
#             ] 



# 방법 1. 브루트 포스로 계산
def solution(self, nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort() # 앞, 뒤가 같은 값이 있을 경우, 이를 쉽게 처리하기 위해 먼저 정렬해줌

    # 브루트 포스 n^3 반복 (문제에서 3개의 엘리먼트를 출력하라고 했기때문에 3번 반복)
    # i를 축으로 하고, 중복된 값을 건너뛰게 한 부분은 다음과 같이 앞서 풀이와 동일함
    for i in range(len(nums) - 2):
        # continue로 중복된 값 건너뛰기
        if 1>0 and nums[i] == nums[i-1]:
            continue

        for j in range(i+1, len(nums) -1):
            if j>i+1 and nums[j] == nums[j-1]:
                continue
            for k in range(j+1, len(nums)):
                if k > j+1 and nums[k] == nums[k-1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:  # 문제의 조건 => 합이 0을 만들어야 함
                    results.append(nums[i],nums[j],nums[k]) # 결과 리스트에 조합 한 숫자씩 append해줌

    return results


# 방법 2. 투 포인터로 합 계산
def solution(self, nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    for i in range(len(nums) -2):
        # 중복된 값 건너뛰기
        if i>0 and nums[i] == nums[i-1]:
            continue
        
        # 간격을 좁혀가며 합 sum 계산
        left, right = i + 1, len(nums) -1 # left는 오른쪽으로 진행 , right는 왼쪽으로 진행 
        while left < right:
            sum = nums[i] + nums[left] + nums[right] 
            if sum < 0: # 앞에서 뒤로 이동 -> 정렬했기 때문에 배열 첫 번째 수가 -임
                left += 1
            elif sum > 0: # 뒤에서 앞으로 이동 
                right -= 1
            else:
                # sum = 0 인 경우이므로 정답 및 스킵 처리
                results.append([nums[i], nums[left], nums[right]]) # 결과 조합의 배열을 results 리스트에 append해줌
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right -1]:
                    right -= 1
                left += 1
                right -= 1

    return results

