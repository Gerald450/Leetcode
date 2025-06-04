class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #create a frequency dic
        #find key that has value > n/2
        
        hashmap = Counter(nums)

        for key, value in hashmap.items():
            if value > (len(nums)/ 2):
                return key

