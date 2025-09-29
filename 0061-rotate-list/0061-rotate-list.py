# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #find length, traverse until len - k
        #newHead = curr.next, curr.next = None, need a pointer at the end
        #end.next = head
        #return newHead
        #length

        if not head:
            return head
        curr, count = head, 0
    

        while curr.next:
            count += 1
            curr = curr.next

        count += 1

        curr.next = head
        #prev points at newHead
        newEnd = head
        for i in range(count - (k % count) - 1):
            newEnd = newEnd.next
        #newEnd points to new end
        newHead = newEnd.next
        newEnd.next = None

        return newHead
        


            

        