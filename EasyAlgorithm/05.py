# 05. 하노이의 탑 옮기기

# ** 원반이 n개인 하노이의 탑을 옮기기 위한 원반 이동 순서를 출력하는 알고리즘을 만들어보세요.



# 방법 -> 재귀 호출 : 원반 1개일 때가 종료 조건
def hanoi(n, start, end, middle):
    if n==1:
        print(start, "->", end)
        return
    # 원반 n-1개를 middle로 이동
    hanoi(n-1, start, middle, end) # end를 보조기둥으로
    print(start, "->", end)

    # middle_pos에 있는 원반 n-1개를 목적지로 이동
    hanoi(n-1, middle, end, start) # start를 보조 기둥으로 