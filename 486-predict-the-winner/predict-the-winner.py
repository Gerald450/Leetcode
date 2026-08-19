class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        cache = {}
        def dfs(l, r) -> int:
            if l == r:
                return nums[l]
            if (l, r) in cache:
                return cache[(l, r)]

            take_left = nums[l] - dfs(l + 1, r)
            take_right = nums[r] - dfs(l, r - 1)

            cache[(l, r)] = max(take_left, take_right)

            return max(take_left, take_right)


        return dfs(0, len(nums) - 1) >= 0


        
        