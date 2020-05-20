# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head, point = None, None
        while l1 or l2:
            if not l2 or (l1 and l1.val <= l2.val):
                if not head:
                    head = l1
                    point = head
                else:
                    point.next = l1
                    point = point.next
                l1 = l1.next
            else:
                if not head:
                    head = l2
                    point = head
                else:
                    point.next = l2
                    point = point.next
                l2 = l2.next
        return head
