class Solution:
    def intToRoman(self, num: int) -> str:
        #make dict
        romanDict = {
            1:"I",
            4:'IV',
            5:'V',
            9:'IX',
            10:'X',
            40:'XL',
            50:'L',
            90:'XC',
            100:'C',
            400:'CD',
            500:'D',
            900:'CM',
            1000:'M'
        }

        #if num has 1,2,3 we divide by 10, 100, 1000
        #if num has 6, 7, 8 we sub 5 and divide by 10, 100, 1000

        if num in romanDict:
            return romanDict[num]
        
        numStr = str(num)
        n = len(numStr) - 1
        total = ''
        for i in numStr:
            dec = int(i) * (10**n)
            if dec in romanDict:
                total += romanDict[dec] 
            else:
                if int(i) > 5:
                    five = 5 * (10**n)
                    total = total + romanDict[five] + (romanDict[10**n] * (int(i)-5))
                elif int(i) < 5:
                    total += romanDict[10**n] * int(i)
            n -= 1
        return total

                    
                


        