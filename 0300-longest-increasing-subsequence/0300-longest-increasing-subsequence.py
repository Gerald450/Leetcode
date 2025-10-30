class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxLen = 0

        def dfs(i, curr):
            nonlocal maxLen
            if i == len(nums):
                maxLen = max(maxLen, len(curr))
                return

            dfs(i + 1, curr)

           
            if not curr or nums[i] > curr[-1]:
                curr.append(nums[i])
                dfs(i + 1, curr)
                curr.pop()


        dfs(0, [])
        return maxLen
