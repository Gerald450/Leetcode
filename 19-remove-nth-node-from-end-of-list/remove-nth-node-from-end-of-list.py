# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        size = 0
        dummy = ListNode()
        dummy.next = head


        #get size:
        while curr:
            curr = curr.next
            size += 1
        


        if n == size:
            return head.next
        #loop till size - n
        curr = head
        #curr -> n - 1
        for _ in range(size - n - 1):
            curr = curr.next
        


        #if n = 1: that's last item
        if n == 1:
            curr.next = None
        else:
            curr.next = curr.next.next

        return dummy.next

        

