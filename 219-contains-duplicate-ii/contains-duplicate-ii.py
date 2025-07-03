class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}

        for i, a in enumerate(nums):
            if a in hashmap:
                for j in hashmap[a]:
                    diff = abs(i - j)
                    if diff <= k:
                        return True
                hashmap[a].append(i)

            hashmap[a] = [i]

        return False
            


        