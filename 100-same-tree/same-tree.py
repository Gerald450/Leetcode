# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True

        arrp = []
        arrq = []

        qq = collections.deque([q])
        qp = collections.deque([p])

        while qq:

            for _ in range(len(qq)):
                node = qq.popleft()
                val = node.val if node else None
                arrq.append(val)
                if node:
                    qq.append(node.left)
                    qq.append(node.right)
        
        while qp:

            for _ in range(len(qp)):
                node = qp.popleft()
                val = node.val if node else None
                arrp.append(val)
                if node:
                    qp.append(node.left)
                    qp.append(node.right)

        print(arrq, arrp)

        return arrp == arrq
            

                

        