# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = newNode = ListNode()

        while list1 and list2:
            v1, v2 = list1.val, list2.val
    

            if v1 < v2:
                newNode.next = ListNode(v1)
                list1 = list1.next

            else:
                newNode.next = ListNode(v2)
                list2 = list2.next

            
            newNode = newNode.next

        newNode.next = list1 or list2

        return dummy.next

        