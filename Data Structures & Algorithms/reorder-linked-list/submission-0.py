# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Idea:
            # 1. Split list into 2 with slow/fast pointers
            # 2. Reverse 2nd half of list
            # 3. Merge 2 lists together

        # Part 1:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Part 2:
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # Part 3
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next

            # Inserting second between first and first.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
