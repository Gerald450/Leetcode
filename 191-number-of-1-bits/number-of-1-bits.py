class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n // 2 != 0:
            if n % 2 == 1:
                count += 1
            n //= 2

        count += 1

        return count



        