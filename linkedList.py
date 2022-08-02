class Node:
    def __init__(self, data) -> None:
        self.val: any = data
        self.next: Node = None


class LinkedList:
    def __init__(self, start: Node) -> None:
        self.start = start
        self.size = 1

    def add(self, data, index: int = None):
        node = self.start
        newNode = Node(data)

        # append to end
        if index == None:
            while node.next != None:
                node = node.next
            node.next = newNode

        # add to beginning
        elif index == 0:
            newNode.next = node
            self.start = newNode

        # add at index
        else:
            node = self.get(index-1)
            newNode.next = node.next
            node.next = newNode

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

    def get(self, index: int):
        node = self.start

        # get from end of list
        if index < 0:
            for i in range(max(0, self.size + index)):
                node = node.next

        # return node from index
        else:
            for i in range(min(index, self.size)):
                node = node.next

        return node

    def printAll(self):
        node = self.start
        for i in range(self.size):
            print('%i: %s' % (i, node.val))
            node = node.next
        print()


l = LinkedList(Node(5))
l.add('hello')
l.add('hi')
l.add('what\'s up')
l.add('first', 0)
l.add('fourth', 4)
l.printAll()

# print(l.get(-5555).val)
