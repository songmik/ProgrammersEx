# 15. 최대 수익 알고리즞ㅁ

# ** 어떤 주식에 대해 특정 기간 동안의 가격 변화가 주어졌을 때, 그 주식을 한 주를 한 번 사고
#    팔아 얻을 수 있는 최대 수익을 계산하는 알고리즘을 만들어 보세요.



# 방법 1. 최대 수익을 구하는 알고리즘
def max(prices):
    n = len(prices)
    max = 0

    for i in range(0, n-1):
        for j in range(i+1, n):
            # i날 사서 j날에 팔았을 때 얻을 수 있는 수익
            profit = prices[j] - prices[i]
            # 이 수익이 지금까지 최대 수익보다 크면 값을 고침
            if profit > max:
                max = profit
    return max


# 방법 2. 
def max(prices):
    n = len(prices)
    max = 0
    min = prices[0] # 첫째 날의 주가를 주가의 최솟값으로 기억해 둠
    for i in range(1, n):
        # 지금까지의 최솟값에 주식을 사서 i날에 팔 때의 수익
        profit = prices[i] - min
        if profit > max: # 이 수익이 지금까지 최대 수익보다 크면 값을 고침
            max = profit
        if prices[i] < min: # i날 주가가 최솟값보다 작으면 값을 고침
            min = prices[i]
    return max



