class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        '''
        input: str of nums, k: int
        output: str of nums

        edge: leading zeros, k >= len(num), not only digits, 

        plan:
        use stack
        pop if find a smaller num, pop whilst it's smaller and num of pops are less than k
        remove any leading zeros from stack
        return stack

        '''

        if k == len(num):
            return '0'
        
        stack = []
        pops = 0

        for digit in num: 
            while stack and int(stack[-1]) > int(digit) and pops < k:
                stack.pop()
                pops += 1
            stack.append(digit)

    
        res_length = len(num) - k
        while len(stack) > res_length:
            stack.pop()
        

        output = ''.join(stack)

        output = output.lstrip('0') or '0'


        return output


        '''
        "1432219", k = 3
               d
        stack = ['1', 2, 1, 9]
        pops = 3
        '1219'

        runtime: O(n)
        space: O(n)
        '''



        