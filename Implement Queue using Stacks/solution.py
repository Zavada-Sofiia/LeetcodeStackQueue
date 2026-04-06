class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.height = 0

    def push(self, value) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.height += 1

    def pop(self) -> int:
        if self.height == 0:
            return None

        temp = self.head
        self.head = self.head.next
        self.height -= 1
        return temp.value

    def peek(self) -> int | None:
        if self.height == 0:
            return None
        return self.head.value

    def empty(self) -> bool:
        return self.height == 0

class MyQueue:
    def __init__(self):
        self.stack1= Stack()
        self.stack2 = Stack()

    def push(self, x: int) -> None:
        self.stack1.push(x)

    def pop(self) -> int:
        if self.stack2.empty():
            while not self.stack1.empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2.empty():
            while not self.stack1.empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()

    def empty(self) -> bool:
        return self.stack1.empty() and self.stack2.empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
