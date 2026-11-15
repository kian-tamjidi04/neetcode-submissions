# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Idea:
            # Find middle of list
            # Reverse 2nd half of the list
            # Merge the 1st half and reversed 2nd half together

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first, second = head, prev

        while second:
            next1, next2 = first.next, second.next
            first.next = second
            second.next = next1

            first = next1
            second = next2

            