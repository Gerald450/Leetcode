# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = head
        prev = dummy

        while curr:
            while curr.next and curr.next.val == curr.val:
                curr = curr.next
            if prev.next != curr:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return dummy.next


  




        




        