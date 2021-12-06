# 23. 큐를 이용한 스택 구현(★)

# ** 큐를 이용해 다음 연산을 지원하는 스택을 구현하라.

"""
 - push(x) : 요소 x를 스택에 삽입한다.
 - pop() : 스택의 첫 번째 요소를 삭제한다.
 - top() : 스택의 첫 번째 요소를 가져온다.
 - empty() : 스택이 비어 있는지 여부를 리턴한다.

 MyStack stack = new Mystack();

 stack.push(1);
 stack.push(2);
 stack.top();   -> 2 리턴
 stack.pop();   -> 2 리턴
 stack.empty();  -> False 리턴

"""


# 방법 : push() 할 때 큐를 이용해 재정렬
class Mystack:
    def __init__(self) :
        self.q = collections.deque() # 큐를 데크로 선언

    def push(self, x):
        self.q.append(x)
        #  요소 삽입 후 맨 앞에 두는 상태로 재정렬
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft()) # 맨 앞 요소를 끄집어낼 때 스택처럼 가장 먼저 삽입한 요소가 나오게 됌

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0