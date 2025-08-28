# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        arr = []
        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next
    

        arr.sort()
        dummy = newList = ListNode(0)

        for i in range(0, len(arr)):
            newList.next = ListNode(arr[i])
            newList = newList.next

        return dummy.next
        

        