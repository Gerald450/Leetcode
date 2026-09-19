class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        input: two str nums
        output: product: str

        edge: zero, leading zero, -gative, empty str

        plan:
        start from leftmost of num2 and multiply with each digit in num1
        get value through ord(num[i]) - ord("0")
        len(num2) - i - 1 = num of trailing zeros
        add trailing before calculating, store carry
        store value in prev and add to the next until done
        final prev is the result

         num2
        xnum1
         456
        x123
        45600

        '''

        def addStrings(str1, str2):
            i = len(str1) - 1
            j = len(str2) - 1
            carry = 0
            res = ""

            while i >= 0 or j >= 0 or carry:
                numA = ord(str1[i]) - ord("0") if i >= 0 else 0
                numB = ord(str2[j]) - ord("0") if j >= 0 else 0

                total = numA + numB + carry
                digit = total % 10
                carry = total // 10

                res = str(digit) + res
                i -= 1
                j -= 1

            return res

        if num1 == "0" or num2 == "0":
            return "0"

        result = "0"

        # Multiply each digit of num1 by num2
        for i in range(len(num1) - 1, -1, -1):
            botNum = ord(num1[i]) - ord("0")
            carry = 0

            # Place-value zeros
            trailZeros = len(num1) - 1 - i
            curr = "0" * trailZeros

            for j in range(len(num2) - 1, -1, -1):
                topNum = ord(num2[j]) - ord("0")

                product = topNum * botNum + carry
                digit = product % 10
                carry = product // 10

                curr = str(digit) + curr

            if carry:
                curr = str(carry) + curr

            result = addStrings(result, curr)

        return result


               



                


                

        