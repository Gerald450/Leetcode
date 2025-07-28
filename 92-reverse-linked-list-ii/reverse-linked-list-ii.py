# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = head

        lst = []

        while head:
            lst.append(head.val)
            head = head.next

        l, r = left - 1, right - 1

        while l <= r:
            lst[l], lst[r] = lst[r], lst[l]
            l += 1
            r -= 1

        newDummy = newNode = ListNode()

        for i in range(len(lst)):
            newNode.next = ListNode(lst[i])
            newNode = newNode.next
        #commit

        return newDummy.next

         
        