import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]

        heapq.heapify(maxHeap)

        for i in range(k):
            res = heapq.heappop(maxHeap)

        return -res


        '''
        maxHeap = [-3, -2, -1, -5, -4]
        heapify = [-5]

        k = 2 -> 2
        res = -5

        



        '''


      

        