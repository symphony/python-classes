class Node:
    def __init__(self, data) -> None:
        self.val = data
        self.next = None


class LinkedList:
    def __init__(self, start: Node) -> None:
        self.start = start
        self.size = 1

    def add(self, data, index: int = None):
        # add to beginning
        if index == 0:
            node = Node(data)
            node.next = self.start
            self.start = node

        # append to end
        elif index == None:
            node = self.start

            while node.next != None:
                node = node.next

            node.next = Node(data)

        # add at index
        else:
            node = LinkedList.get(index - 1)
            node.next = data

        self.size += 1
        return self.size

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
            self.size -= 1

        return self.size

    def get(self, index: int = None):
        node = self.start

        # print all nodes in list
        if index == None:
            for i in range(self.size):
                print('%i: %s' % (i, node.val))
                node = node.next
            return

        for i in range(index):
            node = node.next

        return node


l = LinkedList(Node(5))
l.add('hello')
l.add('hi')
l.add('what\'s up')
l.get()
