# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Idea
            # 1. Split the list in half
            # 2. Reverse the 2nd half
            # 3. Merge the 1st and newly reversed 2nd half to produce the result

        # Part 1 - find midpoint
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        # Part 2 - reverse 2nd half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # Part 3 - merge head and second
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

        

