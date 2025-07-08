class Solution:
    def isHappy(self, n: int) -> bool:
        
        otp = []
        total = n


        while total != 1:



            strs = str(total)

            if total == 7:
                return True


            if len(strs) == 1 and total != 1:
                return False
    
            total = 0

            for num in strs:
                total += (int(num)**2)

    

        return True
            


        