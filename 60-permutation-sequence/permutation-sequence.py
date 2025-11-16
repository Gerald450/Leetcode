from math import factorial
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n + 1)]
        otp = []
        k-=1

        for i in range(n, 0, -1):
            f = factorial(i - 1)
            pos = k // f
            k = k % f
            otp.append(str(nums.pop(pos)))

        return ''.join(otp)

            

        