class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        '''
        input: string s of DNA sequences
        output: array of sequences that appear more than once

        edge: None appear once, s is empty, uppercase/lowercase

        plan:
        use sliding window
        use seen hashmap to detect if sequence appeared again
        add to output set if appears more than once
        convert set to list
        return list
        '''

        l = 0
        seen = set()
        output = set()

        for r in range(9, len(s)):
            sequence = s[l: r + 1]
            if sequence in seen:
                output.add(sequence)
            else:
                seen.add(sequence)
            l += 1

        return list(output)

    '''
    "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
                       l.       r
    sequence = 'AAAAACCCCC'
    seen = {'AAAAACCCCC', 'AAAACCCCCA',...., CCCCCAAAAA,....}
    output = { AAAAACCCCCC, CCCCCAAAAA}

    '''


