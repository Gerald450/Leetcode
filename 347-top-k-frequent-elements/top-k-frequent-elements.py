from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        input: nums -> arr, k -> int
        output: top k most freq

        edge cases: same freq

        plan:
        make a freqDict
        bucket sort: -> arr of arr
            arr of length nums
            put num at arr[value]

        '''

        freqDict = Counter(nums)
        otp = []

        bucket = [[] for _ in range(len(nums) + 1)]

        for key, value in freqDict.items():
            bucket[value].append(key)
        
        #[[], [], [3], [], [1, 2]]

        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                 for num in bucket[i]:
                    otp.append(num)
                    if len(otp) == k:
                        return otp
        return otp

        '''
        freqDict = {
            1:4,
            2:4,
            3:2
        }

        bucket = [[], [], [3], [], [1, 2], [], [], [], [], [], []]





        '''


    


        