class Solution:
    def decodeString(self, s: str) -> str:
        '''
        input: string
        output: decoded string

        use stack
        Fo r
        put in stack until ]
        start poping until [, save that in substr
        pop [
        pop while isDigit and inbound
        save that in num
        add num * substr to stack

        return stack

        '''

        stack = []

        for char in s:
            if char == ']':
                substr = ''
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                
                stack.append(int(num) * substr)
            else:
                stack.append(char)
        
        return ''.join(stack)



'''
3[a2[c]]
       ^
stack = [accaccacc]
substr = 'acc'
num = '3'




'''
