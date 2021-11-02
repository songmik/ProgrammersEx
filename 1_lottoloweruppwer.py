# 가장 좋아요를 많이 받은 풀이

def solution(lottos, win_nums):
    rank=[6,6,5,4,3,2,1]
    cnt=lottos.count(0)
    ans=0

    for i in win_nums:
        if i in lottos:
            ans +=1

    return rank[cnt+ans],rank[ans]