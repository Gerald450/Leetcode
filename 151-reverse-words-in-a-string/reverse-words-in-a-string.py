class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.split()

        otp = ''

        for idx, word in enumerate(res):
            if idx == 0:
                otp = word
            else:
                otp = word + " " + otp

        return otp



       
