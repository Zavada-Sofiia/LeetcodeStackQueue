class FreqNode:
    def __init__(self, value):
        self.value = value
        self.frequency = 1
        self.next = None
        
class StackNode:
    def __init__(self, value, frequent_node):
        self.value = value
        self.frequent_node = frequent_node
        self.next = None

class FreqStack:
    def __init__(self):
        self.frequent_head = None
        self.stack_head = None

    def get_frequent_node(self, value):
        current = self.frequent_head
        previous = None

        while current:
            if current.value == value:
                return current
            previous = current
            current = current.next

        new_node = FreqNode(value)

        if previous:
            previous.next = new_node
        else:
            self.frequent_head = new_node

        return new_node

    def push(self, value: int) -> None:
        node = self.get_frequent_node(value)

        node.frequency += 1

        new_node = StackNode(value, node)
        new_node.next = self.stack_head
        self.stack_head = new_node

    def pop(self) -> int:
        max_frequency = 0
        current = self.frequent_head

        while current:
            if current.frequency > max_frequency:
                max_frequency = current.frequency
            current = current.next

        current = self.stack_head
        previous = None

        while current:
            if current.frequent_node.frequency == max_frequency:
                if previous:
                    previous.next = current.next
                else:
                    self.stack_head = current.next

                current.frequent_node.frequency -= 1
                return current.value

            previous = current
            current = current.next


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
