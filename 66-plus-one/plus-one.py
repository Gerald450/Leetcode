class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''

        for digit in digits:
            num += str(digit)

        num = int(num)
        num += 1
        num = str(num)
        otp = []

        for n in num:
            otp.append(int(n))

        return otp

        