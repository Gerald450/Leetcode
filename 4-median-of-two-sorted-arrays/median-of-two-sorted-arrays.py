class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        n1, n2 = 0, 0
 

        #merge
        while n1 < len(nums1) and n2 < len(nums2):
            v1, v2 = nums1[n1], nums2[n2]

            if v1 < v2:
                nums3.append(v1)
                n1 += 1
            else:
                nums3.append(v2)
                n2 += 1
        
        nums3.extend(nums1[n1:])
        nums3.extend(nums2[n2:])


        n = len(nums3)

        if n % 2 == 0:
            idx = (n - 1) // 2
            return (nums3[idx] + nums3[idx + 1]) / 2
        else:
            return nums3[(n - 1) // 2]