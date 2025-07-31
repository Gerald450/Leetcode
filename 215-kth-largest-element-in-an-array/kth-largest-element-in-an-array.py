import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums) + 1
        heapq.heapify(nums)

        for i in range(n - k):
            otp = heapq.heappop(nums)

        return otp

        