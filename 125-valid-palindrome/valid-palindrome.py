class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        otp = []


        def isAlnum(letter):
            return (ord('a') <= ord(letter) <= ord('z') or ord('0') <= ord(letter) <= ord('9')      or ord('A') <= ord(letter) <= ord('Z'))
                
            

        for letter in s:
            if isAlnum(letter):
                otp.append(letter.lower())

        l, r = 0, len(otp) - 1


        while l < r:
            if otp[l] != otp[r]:
                return False
            l += 1
            r -= 1

        return True
        