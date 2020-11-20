class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        tmp = self.head
        linked_list = ''

        while tmp:
            linked_list += (str(tmp.data) + ' ')
            tmp = tmp.next

        print(linked_list)

    def countList(self):
        tmp = self.head
        count = 0
        while tmp:
            tmp = tmp.next
            count += 1

        return count

    def insertNode(self, value, position=0):
        newNode = Node(value)

        if position == 0:
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode

            return
