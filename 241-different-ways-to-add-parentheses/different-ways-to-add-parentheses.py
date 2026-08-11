class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        '''
        input: str
        output: list[int]

        edge: no operator, negative num, empty

        plan:
        recursion
        treat each operator as the final operator
        split left, and right and get their outcomes and add them to global list


        [2, 3, 4], [4, 5]
        [8, 10, 12, 15, 16, 20]
        '''


        def dfs(partial):
            if partial.isnumeric():
                return [int(partial)]

            res = []
            for idx, char in enumerate(partial):
                if char == "+":
                    left = dfs(partial[:idx])
                    right = dfs(partial[idx + 1:])
                    for i in range(len(left)):
                        for j in range(len(right)):
                            res.append(left[i] + right[j])

                elif char == "-":
                    left = dfs(partial[:idx])
                    right = dfs(partial[idx + 1:])
                    for i in range(len(left)):
                        for j in range(len(right)):
                            res.append(left[i] - right[j])
                
                elif char == "*":
                    left = dfs(partial[:idx])
                    right = dfs(partial[idx + 1:])
                    for i in range(len(left)):
                        for j in range(len(right)):
                            res.append(left[i] * right[j])

            return res
          
        return dfs(expression)

        '''
        "2-1-1"
          ^

        left = "2" => [2]
        right = "1-1" => [0]
                  ^
            left = [1]
            right = [1]
            res = 0

        
        runtime: exponential
        additional space: exponential plus O(n) recursion stack
        '''
        