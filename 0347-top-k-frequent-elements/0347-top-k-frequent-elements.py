class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        freqMap = collections.Counter(nums)

        maxHeap = []
        otp = []

        for key, value in freqMap.items():
            heapq.heappush(maxHeap, (-value, key))

        for _ in range(k):
            freq, num = heapq.heappop(maxHeap)
            otp.append(num)

        return otp
    

        