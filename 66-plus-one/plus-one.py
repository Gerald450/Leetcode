class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()

        carry = 0
        print(digits)

        for idx, digit in enumerate(digits):
            total = digit + carry 
            if idx == 0:
                total += 1


            carry = total // 10
            total = total % 10
           
    

            digits[idx] = total
            

        if carry:
            digits.append(carry)

        digits.reverse()

        return digits


        