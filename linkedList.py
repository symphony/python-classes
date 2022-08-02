class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, start: Node) -> None:
        self.start = start

    def add(self, index: int, data):
        # add to beginning
        if index == 0:
            node = Node(data)
            node.next = self.start
            self.start = node
        # add at index
        else:
            node = LinkedList.get(index - 1)
            node.next = data

    def append(self, data):
        node = self.start
        while node.next != None:
            node = node.next
        node.next = Node(data)

    def delete(self, index: int):
        # delete beginning
        if index == 0:
            self.start == self.start.next
        # delete at index
        else:
            node = self.start
            for i in range(index - 1):
                node = node.next

            toDelete = node.next
            node.next = toDelete.next
            toDelete.next = None

    def get(self, index: int):
        node = self.start
        for i in range(index):
            node = node.next
        return node


n1 = Node(5)
