class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #add open brackets only if open < n
        #add closed brackets only if closed < open
        #valid if open == closed == n
        stack = []
        otp = []
       
        def backtrack(openN, closedN):
            
            if openN == closedN == n:
                otp.append("".join(stack))
                return 
            
            if openN < n:
                stack.append("(")
                backtrack(openN+1,closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN,closedN+1)
                stack.pop()
        
        backtrack(0,0)
        return otp