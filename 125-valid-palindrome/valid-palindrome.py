class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        otp = []

        for letter in s:
            if letter.isalnum():
                otp.append(letter.lower())
                
        l, r = 0, len(otp) - 1

        while l < r:
            if otp[l] != otp[r]:
                return False
            l += 1
            r -= 1

        return True
        