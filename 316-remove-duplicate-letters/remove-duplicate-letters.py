class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        '''
        input: str s
        ouput: str with no duplicates

        edge: empty str, str already has no dups, a mix of ascii chars

        plan:
        use a stack
        while prev letter is greater than curr and can be added at a later time, pop it
        set for seen
        hashmap for greatest index{
            loop through s
            equate the index as the value
            after the loop the curr index should be the greatest
        }
        return stack
        '''
        
        stack = [] #(index, letter)
        in_stack = set()
        greatest_idx = {}

        for idx, letter in enumerate(s):
            greatest_idx[letter] = idx
       
     
        for idx, letter in enumerate(s):
            
            while stack and stack[-1][1] >= letter and idx < greatest_idx[stack[-1][1]] and letter not in in_stack:
                in_stack.remove(stack[-1][1])
                stack.pop()
                

            if letter not in in_stack:
                stack.append((idx, letter))
                in_stack.add(letter)

        output = []
        for tup in stack:
            _, letter = tup
            output.append(letter)


        return ''.join(output)

    


        '''
        stack = []
        greatest_idx = {
            b:3
            c:4
            a:2
        }

        stack = [(0, b)]
        letter = c
        stack = [(0, b), (1, c)]
        letter = a
        greatest_idx[c] = 4
        1 < 4
        stack = [(0, b)]
        b > a, 0 < 3
        stack = [(2, a),(3, b), (4, c)]

        '''


