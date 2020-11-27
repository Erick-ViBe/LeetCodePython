"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]

Explanation: 342 + 465 = 807.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        answer = ListNode()
        pointer = answer
        carry = 0
        summ = 0

        while l1 or l2:
            summ = carry

            if l1:
                summ += l1.val
                l1 = l1.next

            if l2:
                summ += l2.val
                l2 = l2.next

            carry = summ//10
            pointer.next = ListNode(summ % 10)
            pointer = pointer.next

        if carry == 1:
            pointer.next = ListNode(1)

        return answer.next


if __name__ == '__main__':
    s = Solution()

    node_11 = ListNode(2)
    node_12 = ListNode(4)
    node_13 = ListNode(3)

    node_11.next = node_12
    node_12.next = node_13

    node_21 = ListNode(5)
    node_22 = ListNode(6)
    node_23 = ListNode(4)

    node_21.next = node_22
    node_22.next = node_23

    answer = s.addTwoNumbers(node_11, node_21)

    while answer:
        print(answer.val)
        answer = answer.next
