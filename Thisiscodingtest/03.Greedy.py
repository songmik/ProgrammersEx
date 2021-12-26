# Chapter 03. 그리디

# 3-1 . 거스름돈 
n = 1260
count = 0 # 초기화

type = [500,100,50,10]

for coin in type:
    count += n//coin
    n %= coin