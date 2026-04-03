class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenght = 0

    def push(self, x):
        new_node = Node(x)

        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.lenght += 1

    def pop(self):
        if not self.head:
            return None
        value = self.head.value
        self.head = self.head.next

        if not self.head:
            self.tail = None
        self.lenght -= 1

        return value

    def peek(self):
        if self.head:
            return self.head.value
        else:
            return None

    def size(self):
        return self.lenght

    def empty(self):
        return self.lenght == 0

class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q1.push(x)

    def pop(self) -> int:
        while self.q1.size() > 1:
            self.q2.push(self.q1.pop())

        result = self.q1.pop()

        self.q1, self.q2 = self.q2, self.q1

        return result

    def top(self) -> int:
        while self.q1.size() > 1:
            self.q2.push(self.q1.pop())

        result = self.q1.pop()

        self.q2.push(result)

        self.q1, self.q2 = self.q2, self.q1

        return result

    def empty(self) -> bool:
        return self.q1.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
