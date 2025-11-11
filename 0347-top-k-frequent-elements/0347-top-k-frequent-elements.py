from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        input: nums -> arr, k -> int
        output: top k most freq

        edge cases: same freq

        plan:
        make a freq dict
        make a maxheap -> [(-freq, num)]
        pop k times, insert to otp
        return otp

        '''

        freqDict = Counter(nums) 

        maxHeap = []

        for key, value in freqDict.items(): #time -> O(n)
            maxHeap.append((-value, key))

        heapq.heapify(maxHeap)
        otp = []

        for i in range(k): #time -> O(k)
            _, key = heapq.heappop(maxHeap) #O(logn)
            otp.append(key)

        return otp

        '''
        freqDict = {
            1: 4,
            2: 4,
            3: 2
        }

        maxHeap = [(-4, 2), (-2, 3)]
        heap = (-4, 2)

        i = 2 -> 2
        otp = [1, 2]

        '''


        