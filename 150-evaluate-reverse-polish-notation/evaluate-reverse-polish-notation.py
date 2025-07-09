class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total, stack = 0, []

        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == '/':
                c, d = stack.pop(), stack.pop()
                stack.append(int(d/c))
            else:
                stack.append(int(token))

        return stack[-1]
        