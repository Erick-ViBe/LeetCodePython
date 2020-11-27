"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head: ListNode) -> ListNode:
        previous_node = None

        while head:
            next_node = head.next
            head.next = previous_node
            previous_node = head
            head = next_node

        return previous_node


if __name__ == '__main__':
    s = Solution()

    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5

    answer = s.reverseList(node_1)

    while answer:
        print(answer.val)
        answer = answer.next
