# 11. 자신을 제외한 배열의 곱(★★)

# ** 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.

# 예제 : 입력 = [1,2,3,4] , 출력 = [24,12,8,6]
# 주의 : 나눗셈을 하지 않고 O(n)에 풀이하라.



# 방법 : 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
def solution(self, nums: List[int]) -> List[int]:
    out = []
    p = 1
    # 왼쪽 곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    p = 1
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums) -1, 0 -1. -1):
        out[i] = out[i] * p
        p = p * nums[i]
    return out

"""

     [a, b, c, d]
1=[1,      a,   a*b,   a*b*c] -> 왼쪽부터 곱함
2=[b*c*d,  c*d, d,     1]     -> 오른쪽부터 곱함
1*2 = [b*c*d, a*c*d, a*b*d, a*b*c] -> 1과2의 각 위치별 곱


    
    
    
    
"""