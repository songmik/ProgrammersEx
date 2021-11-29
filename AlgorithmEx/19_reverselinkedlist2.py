# 19. 역순 연결 리스트 2(★★)

# ** 연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라. 공간 복잡도 O(1), 시간 복잡도 O(n)에 풀이하라.

# 예제 1. 입력 = 1->2->3->4->5->NULL, 출력 = 1->3->5->2->4->NULL
# 예제 2. 입력 = 2->1->3->5->6->4->7->NULL, 출력 = 2->3->6->7->1->5->4->NULL

# 방법 . 반복 구조로 논드 뒤집기
def solution(self, head: ListNode, m:int, n:int) -> ListNode:
    # 예외 처리
    if not head or m == n:
        return head
    
    root = start = ListNode(None)
    root.next = head

    # start, end 지정
    for _ in range(m -1):
        start = start.next
    end = start.next

    # 반복하며 노드 차례대로 뒤집기
    for _ in range (n - m):
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp
    return root.next
    

