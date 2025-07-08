class Solution:
    def isHappy(self, n: int) -> bool:
        
        otp = []
        total = n
        seen = set()


        while total != 1:
            if total in seen:
                return False
            seen.add(total)

            strs = str(total)
            total = 0

            for num in strs:
                total += (int(num)**2)

    
        return True
            


        