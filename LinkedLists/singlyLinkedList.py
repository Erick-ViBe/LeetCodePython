class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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

    def insertNode(self, value, position=0):
        newNode = Node(value)

        if position == 0:
            newNode.next = self.head
            self.head = newNode
            return

        def getPrevious(position):
            tmp = self.head
            count = 1
            while count < position:
                tmp = tmp.next
                count += 1
            return tmp

        previous = getPrevious(position)
        nextNode = previous.next

        previous.next = newNode
        newNode.next = nextNode

    def deleteNode(self, dataToDelete):
        tmp = self.head

        if tmp is None:
            return

        if tmp.data == dataToDelete:
            self.head = tmp.next
            tmp = None
            return

        while tmp.next.data != dataToDelete:
            tmp = tmp.next

        deletedNode = tmp.next
        tmp.next = deletedNode.next
        deletedNode = None

if __name__ == '__main__':

    #Node structure: 5 -> 1 -> 3 -> 7

    linked_list = LinkedList()

    linked_list.insertNode(7)
    linked_list.insertNode(3)
    linked_list.insertNode(1)
    linked_list.insertNode(5)

    linked_list.printList()

    linked_list.deleteNode(1)

    linked_list.printList()
