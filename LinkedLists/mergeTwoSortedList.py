"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""

class ListNode(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        current = ListNode()
        answer = current

        while l1 and l2:
            if l1.val > l2.val:
                current.next = l2
                l2 = l2.next
            else:
                current.next = l1
                l1 = l1.next

            current = current.next

        while l1:
            current.next = l1
            l1 = l1.next
            current = current.next

        while l2:
            current.next = l2
            l2 = l2.next
            current = current.next

        return answer.next


if __name__ == '__main__':
    s = Solution()

    l1_1 = ListNode(1)
    l1_2 = ListNode(2)
    l1_4 = ListNode(4)

    l1_1.next = l1_2
    l1_2.next = l1_4

    #l1: 1 -> 2 -> 4

    l2_1 = ListNode(1)
    l2_3 = ListNode(3)
    l2_4 = ListNode(4)

    l2_1.next = l2_3
    l2_3.next = l2_4

    #l2: 1 -> 3 -> 4

    answer = s.mergeTwoLists(l1_1, l2_1)

    while answer:
        print(answer.val)

        answer = answer.next
