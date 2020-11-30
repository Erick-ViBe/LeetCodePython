"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.


Example:

    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]

    Explanation: The linked-lists are:
    [   1->4->5,
        1->3->4,
        2->6        ]

    Merging them into one sorted list:
        1->1->2->3->4->4->5->6
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
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

    def mergeKLists(self, lists) -> ListNode:
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None

        last = len(lists)-1

        while last != 0:
            i = 0
            j = last

            while j > i:
                lists[i] = self.mergeTwoLists(lists[i], lists[j])
                i += 1
                j -= 1
                last = j

        return lists[0]

if __name__ == '__main__':
    s = Solution()

    first_1 = ListNode(1)
    first_2 = ListNode(4)
    first_3 = ListNode(5)

    first_1.next = first_2
    first_2.next = first_3

    second_1 = ListNode(1)
    second_2 = ListNode(3)
    second_3 = ListNode(4)

    second_1.next = second_2
    second_2.next = second_3

    third_1 = ListNode(2)
    third_2 = ListNode(6)

    third_1.next = third_2

    x = [first_1, second_1, third_1]

    answer = s.mergeKLists(x)

    print(answer)
