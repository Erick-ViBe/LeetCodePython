"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head: ListNode) -> bool:
        quick = head
        slow = head

        while slow and quick and quick.next:
            quick = quick.next.next
            slow = slow.next

            if slow == quick:
                return True

        return False

class Solution2(object):
    def hasCycle(self, head: ListNode) -> bool:
        try:
            quick = head.next
            slow = head

            while slow is not quick:
                slow = slow.next
                quick = quick.next.next

            return True
        except:
            return False

if __name__ == '__main__':
    s = Solution()

    node_1 = ListNode(1)
    node_5 = ListNode(1)
    node_11 = ListNode(1)
    node_8 = ListNode(1)
    node_9 = ListNode(1)

    node_1.next = node_5
    node_5.next = node_11
    node_11.next = node_8
    node_8.next = node_9
    node_9.next = node_5

    answer = s.hasCycle(node_1)

    print(answer)

    print('************************************')

    s2 = Solution2()

    node_1 = ListNode(1)
    node_5 = ListNode(1)
    node_11 = ListNode(1)
    node_8 = ListNode(1)
    node_9 = ListNode(1)

    node_1.next = node_5
    node_5.next = node_11
    node_11.next = node_8
    node_8.next = node_9
    node_9.next = node_5

    answer = s2.hasCycle(node_1)

    print(answer)
