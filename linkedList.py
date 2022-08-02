from turtle import end_fill


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self._next

    def next(self, data):
        # setter
        if data:
            self._next = Node(data)
        # getter
        else:
            return self._next


class LinkedList:
    def __init__(self, start) -> None:
        self.start = start

    def add(self, index, data):
        if (index == 0):
            node = Node(data)
            node.next(self.start)
            self.start = node
        else:
            node = LinkedList.get(index - 1)
            node.next(data)

    def delete(self):
        pass

    def get(self, index):
        node = self.start
        for i in range(index):
            node = node.next()
        return node


n1 = Node(5)
