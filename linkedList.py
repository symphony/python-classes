class Node:
    def __init__(self, data) -> None:
        self.val: any = data
        self.next: Node = None


class LinkedList:
    def __init__(self, start: Node) -> None:
        self.start = start
        self.size = 1

    def add(self, data, pos: int = None):
        node = self.start
        newNode = Node(data)

        # append to end
        if pos == None:
            while node.next != None:
                node = node.next
            node.next = newNode

        # add to beginning
        elif pos == 0:
            newNode.next = node
            self.start = newNode

        # add at position
        else:
            node = self.get(pos-1)
            newNode.next = node.next
            node.next = newNode

        self.size += 1
        return self.size

    def delete(self, pos: int):
        toDelete = self.start

        # delete beginning
        if pos == 0:
            self.start = toDelete.next

        # delete at position
        else:
            for i in range(pos-1):
                node = node.next

            toDelete = node.next
            node.next = toDelete.next

        # unlink deleted node
        toDelete.next = None
        self.size -= 1
        return self.size

    def get(self, pos: int):
        node = self.start

        # get from end of list
        if pos < 0:
            for i in range(max(0, self.size + pos)):
                node = node.next

        # return node from pos
        else:
            for i in range(min(pos, self.size-1)):
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
print(l.add('last', 36))
l.add('fourth', 3)
l.printAll()

print(l.get(444444).val)
print(l.get(-255).val)
