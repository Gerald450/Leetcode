class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        

        def dfs(l, r) -> int:
            if l == r:
                return nums[l]

            take_left = nums[l] - dfs(l + 1, r)
            take_right = nums[r] - dfs(l, r - 1)

            return max(take_left, take_right)
          


            
        


        return dfs(0, len(nums) - 1) >= 0


        
        