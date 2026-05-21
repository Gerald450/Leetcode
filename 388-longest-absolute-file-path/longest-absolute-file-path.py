class Solution:
    def lengthLongestPath(self, input: str) -> int:
        '''
        input: string of filepath
        output: length of longest past

        edge: no file

        plan:
        use stack
        split by \n
        pop if we on same level
        num_items_to_pop = size of stack - curr_level
        add if we going deeper
        keep track of max size
        '''
        def count(strs):
            count = 0
            for string in strs:
                if string == '\t':
                    count += 1
            return count


        input_arr = input.split('\n')
        stack = []
        maxlength = 0
        curr_level = 0

        for dir in input_arr:
            
            incoming = count(dir)
            #remove trailing \t's
            dir = dir.strip('\t')
            if incoming <= curr_level:
                pops = len(stack) - incoming
                for _ in range(pops):
                    stack.pop()
            
            stack.append(dir)
            if '.' in dir:
                length = len(''.join(stack)) + len(stack) - 1
                maxlength = max(maxlength, length)
            
            curr_level = incoming
            

        return maxlength

        '''
        input_arr = [file1.txt, file2.txt, longfile.txt]


        '''
                
