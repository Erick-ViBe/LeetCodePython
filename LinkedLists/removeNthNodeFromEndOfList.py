"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

Example:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        answer = ListNode()
        answer.next = head

        first = answer
        second = answer

        for i in range(n+1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return answer.next


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

    answer = s.removeNthFromEnd(node_1, 2)

    while answer:
        print(answer.val)
        answer = answer.next
