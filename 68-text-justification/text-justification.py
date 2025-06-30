class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        otp = []
        length, line = 0, []
        i = 0

        while i < len(words):
            if len(words[i]) + len(line) + length > maxWidth:

                extraSpaces = maxWidth - length
                spaces = extraSpaces // max(1, len(line) - 1)
                remainder = extraSpaces % max(1, len(line) - 1)

                for j in range(max(1, len(line) - 1)):
                    line[j] += ' ' * spaces
                    if remainder:
                        line[j] += ' '
                        remainder -= 1
                
                otp.append(''.join(line))
                length, line = 0, []

            
            line.append(words[i])
            length += len(words[i])
            i += 1

        
        #last line
        lastLine = ' '.join(line)
        otp.append(lastLine + ' ' * (maxWidth - len(lastLine)))

        return otp


        

                    
                    


            


                
                



        