# 15. 역순 연결 리스트(★)

# ** 연결 리스트를 뒤집어라.

# 예제 : 입력 = 1->2->3->4->5->NULL , 출력 = 5->4->3->2->1->NULL



# 방법 1. 재귀 구조로 뒤집기
def solutionList(self, head:ListNode) -> ListNode:
    def solution(node: ListNode, prev: ListNode = None): # 다음 노드 next와 현재 노드 node를 파라미터로 지정 -> 계속 호출
        if not node: 
            return prev # node.next에는 이전 prev 리스트를 계속 연결 -> node가 None이 될 때까지 호출
        next, node.next = node.next, prev 
        return solution(next, node) # 백트래킹되며 연결 리스트가 거꾸로 연결
    return solution(head) 


# 방법 2. 반복 구조로 뒤집기
def solution(self, head:ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev # 이전 prev 리스트로 계속 연결하면서 끝날 때까지 반복
        prev, node = node, next

    return prev