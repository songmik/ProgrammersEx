# 24. 스택을 이용한 큐 구현(★)

# ** 스택을 이용해 다음 연산을 지원하는 큐를 구현하라.

"""
 - push(x) : 요소 x를 큐 마지막에 삽입한다.
 - pop() : 큐 처음에 있는 요소를 제거한다.
 - peek() : 큐 처음에 있는 요소를 조회한다.
 - empty() : 큐가 비어 있는지 여부를 리턴한다.

 MyQueue stack = new MyQueue();

 queue.push(1);
 queue.push(2);
 queue.peek();   -> 1 리턴
 queue.pop();   -> 1 리턴
 queue.empty();  -> False 리턴 

"""



# 방법 : 스택 2개 사용
class MyQueue:
    def __init__(self) :
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        # output이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
    
    def empty(self):
        return self.input ==[] and self.output == []
        