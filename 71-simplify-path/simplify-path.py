class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        i = 0
        print(path)
        while i < len(path):
            while i < len(path) and  path[i] == '':
                i += 1
            if i >= len(path):
                break
            
            print(stack)
            if path[i] == '.':
                i += 1
            elif path[i] == '..':
                if stack:
                    stack.pop()
                i += 1
            else:
                
                stack.append('/' + path[i])
                i += 1


        return ''.join(stack) if stack else '/'

        