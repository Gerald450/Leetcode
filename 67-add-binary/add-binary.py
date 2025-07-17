class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        l, r = len(a) - 1, len(b) - 1
        res = ''
        


        while l > -1 or r > -1 or carry:
            v1 = int(a[l]) if l > -1 else 0
            v2 = int(b[r]) if r > -1 else 0

            total = v1 + v2 + carry
            carry = total // 2
            total %= 2

            res += str(total)
            l -= 1
            r -= 1

        return res[::-1]

        




