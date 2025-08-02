class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0

        bits = ''

        while n // 2 != 0:
            bits += str(n % 2)
            n = n // 2
        
        bits += "1"

        bits = bits[::-1].zfill(32)
        
        otp = 0
        #commit

        for i in range(len(bits)):
            if bits[i] == '1':
                otp  += 2**i

        return otp
            

        