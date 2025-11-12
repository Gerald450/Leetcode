from math import factorial
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n+1)]

        k -= 1

        res = []
        for i in range(n, 0, -1):
            f = factorial(i - 1)
            idx = k // f
            k = k % f
            res.append(str(nums.pop(idx)))

        return "".join(res)


        