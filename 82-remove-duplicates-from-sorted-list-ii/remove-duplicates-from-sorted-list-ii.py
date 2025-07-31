# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        dummy = newList = ListNode()

        while head:
            arr.append(head.val)
            head = head.next

        dic = collections.Counter(arr)

        for key, value in dic.items():
            if value == 1:
                newList.next = ListNode(key)
            
                newList = newList.next
        
        return dummy.next





        