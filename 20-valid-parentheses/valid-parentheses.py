class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        stack = []

        for p in s:
            if p in brackets:
                if not stack:
                    return False

                if stack[-1] != brackets[p]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(p)

        return False if stack else True
