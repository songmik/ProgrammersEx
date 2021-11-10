# 주식을 사고팔기 가장 좋은 시젖ㅁ

# ** 한 번의 거래로 낼 수 있는 최대 이익을 산출하라.

# 예제 : 입력 = [7,1,5,3,6,4], 출력 = [5]
# 설명 : 1일 때 사서 6일 때 팔면 5의 이익을 얻는다.



# 방법 1. 브루트 포스로 계산 (사고 팔고를 반복하다보면, 최대 이익을 산출할 수 있을 것 같아서)
def solution(self, prices: List[int]) -> int:
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price


# 방법 2. 저점과 현재 값과의 차이 계산
def solution(self, prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    # 최솟값과 최댓값을 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit

    
