# 예산 https://programmers.co.kr/learn/courses/30/lessons/12982

# 가장 짧은 풀이
def solution(d, budget):
    d.sort()
    while budget < sum(d): # 전체 부서별 신청 금액(sum(d))보다 예산(budget)이 클 때
        d.pop() # 가장 큰 금액을 pop함 
    return len(d) # 예산 내에서 모든 부서를 지원할 수 있을 때 부서의 수를 리턴해줌

# sort() : 리스트를 정렬, 기본값은 오름차순 정렬
# 참고 : https://wikidocs.net/16041

# pop() : 리스트의 요소를 꺼내줌 
# 참고 : https://wikidocs.net/14